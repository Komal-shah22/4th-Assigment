import requests

def get_weather(city):
    """
    Fetches weather details for a given city using OpenWeatherMap API.
    """
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {"q": city, "appid": API_KEY, "units": "metric"}  # Fetch data in Celsius
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌍 Weather in {city.capitalize()}:")
        print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"🌬️ Wind Speed: {wind_speed} m/s")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌥️ Condition: {weather_desc}")
    else:
        print("❌ Error: Unable to fetch weather details. Please check the city name.")

# Welcome message
print("\n🌤️ Welcome to the Weather Finder! 🌎")
print("Get real-time weather updates for any city worldwide!\n")

while True:
    city_name = input("🏙️ Enter a city name: ").strip()
    
    if not city_name.isalpha():
        print("❌ Invalid input! Please enter a valid city name (without numbers or symbols).")
        continue
    
    get_weather(city_name)

    again = input("\n🔄 Do you want to check another city? (yes/no): ").strip().lower()
    if again != "yes":
        print("\n✨ Thank you for using the Weather Finder! Stay updated! 😊✨")
        break
