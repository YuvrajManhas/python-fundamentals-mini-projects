from weather import get_weather
from display import display
import json

city = input("Enter the city name: ")

response = get_weather(city)
with open("weather_history.json") as file:
    old_data = json.load(file)

with open("weather_history.json", "w") as file:
    if response:
        display(response)
        old_data.append(response)
        json.dump(old_data, file, indent = 4)
    else:
        print("City not found.")
 