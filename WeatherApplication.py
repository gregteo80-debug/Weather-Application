import tkinter as tk
import requests

window = tk.Tk()
window.geometry("600x600")
window.title("Weather Application")
window.resizable(False,False)
window.configure(bg="#143CED")

label = tk.Label(window,text="Weather Application",font=("Ms Sans Serif",20,"bold"),bg="#143CED",fg="white")
label.pack(pady=20)

labelCity = tk.Label(window,text="Enter the city name:",font=("Ms Sans Serif",15,"underline"),bg="#143CED",fg="white")
labelCity.pack(pady=10)

entry = tk.Entry(window,width=30,font=("Ms Sans Serif",15,"bold"),bg="#143CED",fg="white")
entry.pack(pady=10)

buttonGetWeather = tk.Button(window,text="Get Weather",font=("Ms Sans Serif",15,"bold"),bg="#143CED",fg="white",width=19,command=lambda: get_Weather(entry.get()))
buttonGetWeather.pack(pady=35)

labelYourWeather = tk.Label(window,text="Your Weather:...",font=("Ms Sans Serif",15,"bold"),bg="#143CED",fg="white")
labelYourWeather.pack(pady=20)

def get_Weather(city):
    try:
        response = requests.get("https://geocoding-api.open-meteo.com/v1/search",params={"name":city},timeout=10)
        if response.status_code == 200:
            data = response.json()
            if "results" in data and len(data["results"]) > 0:
                latidude = data["results"][0]["latitude"]
                longiteude = data["results"][0]["longitude"]
                response2 = requests.get("https://api.open-meteo.com/v1/forecast",timeout=10,params={"latitude": latidude,"longitude": longiteude,"current":"temperature_2m"})
                if response2.status_code == 200:
                    dataa = response2.json()
                    labelYourWeather.config(text=f"Your city was {city}.\nLatitude: {latidude}.\nLongitude: {longiteude}.\nTemperature:  {dataa["current"]["temperature_2m"]}")
                else:
                    labelYourWeather.config(text="Error in server...")
            else:
                labelYourWeather.config(text="Your city was not found")
        else:
            labelYourWeather.config(text="Error in server...")
    except:
        labelYourWeather.config(text="Error in server")

window.mainloop()
