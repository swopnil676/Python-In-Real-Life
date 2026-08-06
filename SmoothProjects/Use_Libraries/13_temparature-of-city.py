import requests

city = input("Enter City name :")

url = f"https://wttr.in/{city}?format=j1"

data = requests.get(url).json()

temp = data["current_condition"][0]["temp_C"]
feels_like = data["current_condition"][0]["FeelsLikeC"]
weather = data["current_condition"][0]["weatherDesc"][0]["value"]
humidity = data["current_condition"][0]["humidity"]

print("\n 🌍 City :", city)
print(" 🌡️ Temperature :", temp, "°C")
print(" 🤔 Feels Like :", feels_like, "°C")
print(" ☁️ Weather :", weather)
print(" 💧 Humidity :", humidity, "%")