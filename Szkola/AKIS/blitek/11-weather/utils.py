import requests

_weatherStations = None
_airQualityStations = None


def _load_weather():
    global _weatherStations
    if _weatherStations is None:
        res = requests.get("https://danepubliczne.imgw.pl/api/data/synop/")
        res.raise_for_status()
        _weatherStations = res.json()
    return _weatherStations


def _load_air():
    global _airQualityStations
    if _airQualityStations is None:
        res = requests.get("https://api.gios.gov.pl/pjp-api/v1/rest/station/findAll?size=1000")
        res.raise_for_status()
        _airQualityStations = res.json()
    return _airQualityStations


def get_cities():
    stations = _load_weather()
    return [s.get("stacja") for s in stations if s.get("stacja")]


def get_weather(city):
    stations = _load_weather()
    for w in stations:
        if w.get("stacja") == city:
            return w
    return None


def _get_air_quality_data(id_):
    res = requests.get(f"https://api.gios.gov.pl/pjp-api/v1/rest/aqindex/getIndex/{id_}")
    res.raise_for_status()
    return res.json()


def get_air_quality(city):
    stations = _load_air()
    for st in stations.get('Lista stacji pomiarowych', []):
        if st.get("Nazwa miasta") == city:
            q = _get_air_quality_data(st.get("Identyfikator stacji"))
            return q.get("AqIndex") if isinstance(q, dict) else None
    return None
