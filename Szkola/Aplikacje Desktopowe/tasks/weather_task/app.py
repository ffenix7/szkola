import tkinter as tk
from tkinter import ttk
import requests
import json

def check_forecast():
    value = city.get()
    result.config(text="")
    for row in data_weather:
        if row['stacja'] == value:
            result.config(text=f"City: {row['stacja']}\n"
                               f"Temperature: {row['temperatura']} °C\n"
                               f"Humidity: {row['wilgotnosc_wzgledna']} %\n"
                               f"Wind speed: {row['predkosc_wiatru']} km/h\n"
                               f"Wind direction: {row['kierunek_wiatru']}°\n"
                               f"Rain: {row['suma_opadu']} mm\n"
                               f"Pressure: {row['cisnienie']} hPa")
    
    all_stations = json.loads(requests.get(f"https://api.gios.gov.pl/pjp-api/v1/rest/station/findAll?size=9999").text)['Lista stacji pomiarowych']
    for row in all_stations:
        if row['Nazwa miasta'] == value:
            stationID = row['Identyfikator stacji']
            #print(stationID)
            sensors = requests.get(f"https://api.gios.gov.pl/pjp-api/v1/rest/station/sensors/{stationID}").json()
            stations = sensors.get('Lista stanowisk pomiarowych dla podanej stacji', [])
            if stations[]


data_weather = requests.get("https://danepubliczne.imgw.pl/api/data/synop").json()
cities = [row['stacja'] for row in data_weather]

#print(data_weather)

root = tk.Tk()

root.title("Weather app")
root.geometry("200x400")

label = tk.Label(root, text="Weather forecast")
label.pack(pady=10)

label_2 = tk.Label(root, text="Choose a city:")
label_2.pack(pady=10)

city = ttk.Combobox(root, values=cities, state="readonly")
city.pack(pady=10)

button = tk.Button(root ,text="Check weather forecast", command=check_forecast)
button.pack(pady=10)

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()