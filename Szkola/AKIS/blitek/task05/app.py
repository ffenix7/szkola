from flask import Flask, jsonify
import os
import pandas as pd


app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
JABLKA_FILE = os.path.join(BASE_DIR, 'jablka.txt')
CENNIK_FILE = os.path.join(BASE_DIR, 'cennik.txt')

MIESIACE = {
    '01': 'Styczen',
    '02': 'Luty',
    '03': 'Marzec',
    '04': 'Kwiecien',
    '05': 'Maj',
    '06': 'Czerwiec',
    '07': 'Lipiec',
    '08': 'Sierpien',
    '09': 'Wrzesien',
    '10': 'Pazdziernik',
    '11': 'Listopad',
    '12': 'Grudzien'
}


def error_response(message, code=500):
    return {
        'status': 'error',
        'code': code,
        'message': message
    }, code


def load_jablka():
    return pd.read_csv(JABLKA_FILE, sep='\t')

def load_cennik():
    return pd.read_csv(CENNIK_FILE, sep='\t')

@app.route('/api/analiza/top-klienci-zimowe')
def top_klienci_zimowe():
    try:
        jablka = load_jablka()
        #print(jablka)
    except Exception as e:
        return error_response(f'Blad wczytywania danych: {e}', 500)

    jablka_zimowe = jablka[jablka['typ'] == 'Z']
    top_klienci = (
        jablka_zimowe
        .groupby('nip', as_index=False)['kg']
        .sum()
        .sort_values('kg', ascending=False)
        .head(3)
    )

    return {
        "status": "success",
        "analiza": "7.1",
        "nazwa": "Top 3 klienci - jablka zimowe",
        "data": {
            "top_klienci": top_klienci.to_dict(orient='records')
        }
    }

@app.route("/api/analiza/przychod")
def przychod():
    try:
        jablka = load_jablka()
        cennik = load_cennik()
    except Exception as e:
        return error_response(f'Blad wczytywania danych: {e}', 500)

    try:
        merged = jablka.merge(
            cennik[["odmiana", "cena"]],
            left_on="odmiana",
            right_on="odmiana",
            how='left'
        )

        merged['kg'] = pd.to_numeric(merged['kg']).fillna(0)
        merged["cena"] = pd.to_numeric(merged["cena"]).fillna(0)

        merged['przychod'] = (merged['kg'] * merged["cena"]).round(2)

        przychod_odmiany = (
            merged.groupby("odmiana", as_index=False)['przychod']
            .sum()
            .round(2)
            .sort_values('przychod', ascending=False)
        )

        calkowity_przychod = round(float(merged['przychod'].sum()), 2)
        odmiana_z_najwiekszym_przychodem = None
        przychod_najlepszej = 0.0
        top_odmiany = []

        if not przychod_odmiany.empty:
            odmiana_z_najwiekszym_przychodem = przychod_odmiany.iloc[0]["odmiana"]
            przychod_najlepszej = round(float(przychod_odmiany.iloc[0]["przychod"]), 2)
            top_odmiany = (
                przychod_odmiany
                .head(3)
                .to_dict(orient='records')
            )

        return {
            'status': 'success',
            'analiza': '7.2',
            'nazwa': 'Przychod i najlepsza odmiana',
            'data': {
                'calkowity_przychod' : calkowity_przychod,
                'najlepsza_odmiana': odmiana_z_najwiekszym_przychodem,
                'przychod_najlepszej':  przychod_najlepszej,
                'top_odmiany': top_odmiany
            }
        }
    except Exception as e:
        return error_response(f'Blad obliczania przychodu: {e}', 500)
    

@app.route('/api/analiza/popularnosc-miesiecy')
def miesiace():
    try:
        jablka = load_jablka()
        cennik = load_cennik()
    except Exception as e:
        return error_response(f'Blad wczytywania danych: {e}', 500)
    
    try:
        jablka['data'] = pd.to_datetime(jablka['data'])
        jablka['kg'] = pd.to_numeric(jablka['kg']).fillna(0)

        jablka['miesiac'] = jablka['data'].dt.strftime('%Y-%m')
        grouped = jablka.groupby(['miesiac', 'odmiana'], as_index=False)['kg'].sum()
        
        results = []
        for m in range(1, 13):
            month_str = f"2022-{m:02d}"
            month_name = MIESIACE.get(f"{m:02d}")
            
            cur = grouped[grouped['miesiac'] == month_str]
            if cur.empty:
                results.append({
                    'miesiac': month_str,
                    'miesiac_nazwa': month_name,
                    'najpopularniejsza': None,
                    'kilogramy': 0
                })
            else:
                top = cur.loc[cur['kg'].idxmax()]
                results.append({
                    'miesiac': month_str,
                    'miesiac_nazwa': month_name,
                    'najpopularniejsza': top['odmiana'],
                    'kilogramy': int(top['kg'])
                })

        return {
            'status': 'success',
            'analiza': '7.3',
            'nazwa': 'Najpopularniejsza odmiana w kazdym miesiacu',
            'data': {
                'miesiace': results
            }
        }
    except Exception as e:
        return error_response(f'Blad obliczania przychodu: {e}', 500)


@app.route('/api/analiza/rabaty')
def rabaty():
    try:
        jablka = load_jablka()
    except Exception as e:
        return error_response(f'Blad wczytywania danych: {e}', 500)

    try:
        jablka['data'] = pd.to_datetime(jablka['data'])
        jablka['kg'] = pd.to_numeric(jablka['kg']).fillna(0)
        jablka = jablka.dropna(subset=['data', 'nip']).sort_values('data')
        stan_klientow = {}
        liczba_transakcji_z_rabatem = 0
        calkowita_wartosc_rabatow = 0.0
        przedzial_5 = {'liczba_transakcji': 0, 'calkowita_wartosc': 0.0}
        przedzial_10 = {'liczba_transakcji': 0, 'calkowita_wartosc': 0.0}

        for _, row in jablka.iterrows():
            nip = row['nip']
            kg = float(row['kg'])
            poprzedni_stan = stan_klientow.get(nip, 0.0)

            if kg <= 0:
                stan_klientow[nip] = poprzedni_stan + kg
                continue

            if poprzedni_stan >= 20000:
                rabat_za_kg = 0.10
            elif poprzedni_stan >= 15000:
                rabat_za_kg = 0.05
            else:
                rabat_za_kg = 0.0

            if rabat_za_kg > 0:
                wartosc_rabatu = round(kg * rabat_za_kg, 2)
                liczba_transakcji_z_rabatem += 1
                calkowita_wartosc_rabatow += wartosc_rabatu
                if rabat_za_kg == 0.05:
                    przedzial_5['liczba_transakcji'] += 1
                    przedzial_5['calkowita_wartosc'] += wartosc_rabatu
                else:
                    przedzial_10['liczba_transakcji'] += 1
                    przedzial_10['calkowita_wartosc'] += wartosc_rabatu

            stan_klientow[nip] = poprzedni_stan + kg

        return {
            'status': 'success',
            'analiza': '7.4',
            'nazwa': 'System rabatow dla klientow hurtowych',
            'data': {
                'liczba_transakcji_z_rabatem': liczba_transakcji_z_rabatem,
                'calkowita_wartosc_rabatow': round(calkowita_wartosc_rabatow, 2),
                'przedzial_5_groszy': {
                    'liczba_transakcji': przedzial_5['liczba_transakcji'],
                    'calkowita_wartosc': round(przedzial_5['calkowita_wartosc'], 2)
                },
                'przedzial_10_groszy': {
                    'liczba_transakcji': przedzial_10['liczba_transakcji'],
                    'calkowita_wartosc': round(przedzial_10['calkowita_wartosc'], 2)
                }
            }
        }
    except Exception as e:
        return error_response(f'Blad obliczania rabatow: {e}', 500)



if __name__ == '__main__':
    app.run(debug=True)