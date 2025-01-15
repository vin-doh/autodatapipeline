import requests
import os
import json

# Weatherstack API details
API_KEY = "311c176ba1e5d0158232b46ff3583660"
BASE_URL = "http://api.weatherstack.com/current"

def fetch_weather(location):
    params = {
        "access_key": API_KEY,
        "query": location
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if "current" in data:
            return data
        else:
            print(f"Error fetching data for {location}: {data.get('error', {}).get('info', 'Unknown error')}")
            return None
    else:
        print(f"HTTP Error {response.status_code} for location: {location}")
        return None

def save_weather_data(data, location):
    os.makedirs("weather_data", exist_ok=True)
    filename = f"{location.lower().replace(' ', '_')}_weather.json"
    filepath = os.path.join("weather_data", filename)
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Weather data for {location} saved to {filepath}")

if __name__ == "__main__":
    # Test example
    location = "London"  # Example location
    weather_data = fetch_weather(location)
    if weather_data:
        save_weather_data(weather_data, location)
