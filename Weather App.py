import requests
API_KEY = "0bd1b97f463b0c6ae4450bf8f4e653fa"

print("--- Weather Forecast App ---\n")

location = input("Enter city name to search: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"

response = requests.get(url,timeout=5)
print(response)

if response.status_code == 200:
    data = response.json()

    city = data["name"]
    weather = data["weather"][0]["description"]
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    print(f"Weather in {city}:")
    print(f"Conditions: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
else:
    print("Error: Unable to fetch weather data. Invalid City.")