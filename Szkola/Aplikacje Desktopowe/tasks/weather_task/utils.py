import requests
import json

allWeatherStationsAPI = "https://danepubliczne.imgw.pl/api/data/synop/"
res = requests.get(allWeatherStationsAPI)
weatherStations = json.loads(res.text)
cities = [stacion["stacja"] for stacion in weatherStations]

allAirQualityStationsAPI = "https://api.gios.gov.pl/pjp-api/v1/rest/station/findAll?size=1000"
res = requests.get(allAirQualityStationsAPI)
airQualityStations = json.loads(res.text)

print(airQualityStations['Lista stacji pomiarowych'])

def getCities():
    return cities

def getWeather(city):
    for weather in weatherStations:
        if weather["stacja"] == city:
            return weather
    return None

def _getAirQualityData(id):
    res = requests.get(f"https://api.gios.gov.pl/pjp-api/v1/rest/aqindex/getIndex/{id}")
    return json.loads(res.text)

def getAirQuality(city):
    for airQuality in airQualityStations['Lista stacji pomiarowych']:
        if airQuality["Nazwa miasta"] == city:
            quality = _getAirQualityData(airQuality["Identyfikator stacji"])["AqIndex"]
            if quality["Nazwa kategorii indeksu"] != None and quality["Nazwa kategorii indeksu dla wskażnika PM2.5"] != None and quality["Nazwa kategorii indeksu dla wskażnika PM10"] != None:
                return quality