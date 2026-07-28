from weather import get_weather
from display import display

city = input("Enter the city name: ")

data = get_weather(city)

if data:
    display(data)
else:
    print("City not found.")
 