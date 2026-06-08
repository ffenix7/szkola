# Rejestr Wykroczeń - Aplikacja Tkinter

**Czas:** 90 minut  
**Punkty:**  10   
**Narzędzie:** Python + Tkinter  

---

## 📋 Opis Zadania

Pracujesz jako developer dla jednostki zajmującej się rejestrującą przekroczenia prędkości. Twoje zadanie to stworzenie graficznego interfejsu (GUI) w Tkinter do analizy danych o wykroczeniach.

---

## 📁 Dostępne Pliki Danych

### `kierowcy.txt`
```
IdOsoby;Imie;Nazwisko;NrRejestracyjny
1;Echo;Ayala;FVX4190
2;Nolan;Stein;DUG5882
...
```
- **IdOsoby** - identyfikator kierowcy (liczba)
- **Imie** - imię kierowcy
- **Nazwisko** - nazwisko kierowcy
- **NrRejestracyjny** - numer rejestracyjny samochodu

### `taryfikator.txt`
```
IdWykroczenia;Wykroczenie;Punkty;Kwota
1;Przekroczenie prędkości do 10 km/h;0;50
2;Przekroczenie prędkości od 11 do 20 km/h;2;100
...
```
- **IdWykroczenia** - identyfikator typu wykroczenia
- **Wykroczenie** - opis wykroczenia
- **Punkty** - liczba punktów karnych
- **Kwota** - wysokość mandatu w zł

### `rejestr.txt`
```
IdZdarzenia;Data;IdOsoby;IdWykroczenia
1;2023-01-01;1;1
2;2023-01-01;2;4
...
```
- **IdZdarzenia** - identyfikator zdarzenia
- **Data** - data wykroczenia (YYYY-MM-DD)
- **IdOsoby** - identyfikator kierowcy
- **IdWykroczenia** - identyfikator typu wykroczenia

---

## 🎯 Wymagania Aplikacji

Stwórz aplikację Tkinter z następującymi funkcjami:

### 1. **Wczytywanie Danych**
- ✅ Wczytaj dane z plików `kierowcy.txt`, `taryfikator.txt` i `rejestr.txt`
- ✅ Parsowanie formatu separowanego średnikami (`;`)
- ✅ Obsługa błędów (plik nie znaleziony, błędny format)

### 2. **Tabela Danych**
- ✅ Wyświetl wszystkie wykroczenia w tabeli (Treeview)
- ✅ Kolumny: ID, Data, Kierowca, Nr Rej., Typ Wykroczenia, Punkty, Kwota
- ✅ Możliwość przewijania (scrollbars)
- ✅ Formatowanie kwot (dwa miejsca po przecinku)

### 3. **Filtrowanie**
- ✅ Filtr po kierowcy (dropdown lista wszystkich kierowców + opcja "Wszyscy")
- ✅ Filtr po typie wykroczenia (dropdown lista + opcja "Wszystkie")
- ✅ Przycisk "Resetuj" do przywrócenia wszystkich danych
- ✅ Dynamiczna aktualizacja tabeli po zmianie filtrów

### 4. **Statystyki**
- ✅ Liczba wyświetlanych wykroczeń
- ✅ Całkowita kwota mandatów
- ✅ Całkowita liczba punktów karnych
- ✅ Najczęstsze wykroczenie (ile razy się pojawiło)
- ✅ Kierowca z największą łączną kwotą mandatów

### 5. **Interfejs i UX**
- ✅ Przejrzysta organizacja elementów
- ✅ Czytelne labels i nagłówki
- ✅ Responsive layout
- ✅ Brak crashy przy braku danych

---

### Oczekiwany Rezultat

Aplikacja powinna:
1. ✅ Załadować się bez błędów
2. ✅ Wyświetlić 200 wykroczeń w tabeli
3. ✅ Pozwolić filtrować po kierowcy i wykroczeniu
4. ✅ Pokazać aktualne statystyki
5. ✅ Być responsywna i czytelna
