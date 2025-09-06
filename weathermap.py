import tkinter as tk
from tkinter import messagebox
import requests


def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    api_key = "9b6b25f783ac3a4ce3b7d2e8ce90584f"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"])
            return
        
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        weather = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        result = f"City: {city_name}, {country}\n"
        result += f"Temperature: {temperature}°C\n"
        result += f"Weather: {weather}\n"
        result += f"Humidity: {humidity}%\n"
        result += f"Wind Speed: {wind_speed} m/s"
        
        result_label.config(text=result)
    
    except Exception as e:
        messagebox.showerror("Error", "Unable to fetch weather data")


root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"))
title_label.pack(pady=10)


city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=5)

search_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
search_button.pack(pady=10)


result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()