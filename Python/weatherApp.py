import requests
import json
import pyttsx3

city = input("Enter the name of city:")

url=f"https://api.weatherapi.com/v1/current.json?key={apikey}&q={city}%27"

r =requests.get(url)
weatherDic=json.loads(r.text)

engine = pyttsx3.init()
engine.say(f"The current temp of {city} is {weatherDic["current"]["temp_c"]} in celcius")
engine.runAndWait()
