import tkinter as tk
from tkinter import ttk
import utils

root = tk.Tk()
root.title("Weather app")
root.geometry("300x300")

label = tk.Label(root, text="Weather forecast")
label.pack(pady=10)

label_2 = tk.Label(root, text="Choose a city:")
label_2.pack(pady=5)

city = ttk.Combobox(root, values=utils.getCities(), state="readonly")
city.pack(pady=5)

result = tk.Label(root, text="", justify="left", anchor="w")
result.pack(pady=10, fill="x", padx=10)

def check_weather():
	selected = city.get()
	if not selected:
		result.config(text="Please choose a city.")
		return
	try:
		weather = utils.getWeather(selected)
	except Exception as e:
		weather = None
	try:
		air = utils.getAirQuality(selected)
	except Exception:
		air = None

	lines = []
	if weather:
		temp = weather.get("temperatura")
		pressure = weather.get("cisnienie")
		lines.append(f"Temperature: {temp} °C" if temp is not None else "Temperature: N/A")
		lines.append(f"Pressure: {pressure} hPa" if pressure is not None else "Pressure: N/A")
	else:
		lines.append("Weather data: not available")

	if air:
		name = air.get("Nazwa kategorii indeksu")
		pm25 = air.get("Nazwa kategorii indeksu dla wskażnika PM2.5")
		pm10 = air.get("Nazwa kategorii indeksu dla wskażnika PM10")
		lines.append(f"Air index: {name or 'N/A'}")
		lines.append(f"PM2.5: {pm25 or 'N/A'} | PM10: {pm10 or 'N/A'}")
	else:
		lines.append("Air quality: not available")

	result.config(text="\n".join(lines))

button = tk.Button(root, text="Check weather forecast", command=check_weather)
button.pack(pady=5)

root.mainloop()