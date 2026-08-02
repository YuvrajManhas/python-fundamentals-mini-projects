def display(data):
    print("\nWeather Report: ")
    print("*" * 30)
    print("City: ", data["name"])
    print("Temperature: ", data["main"]["temp"], "°C")
    print("Humidity: ", data["main"]["humidity"], "%")
    print("Condition: ", data["weather"][0]["description"])
    print("Feels like: ", data["main"]["feels_like"],"°C")