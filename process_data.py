import os
import json
import csv
from datetime import datetime

def process_weather_data(json_folder, csv_file):
    """
    Process all JSON files in a folder into a single CSV file.

    Args:
        json_folder (str): Path to the folder containing JSON files.
        csv_file (str): Path to save the processed CSV file.
    """
    # CSV header
    header = ["Location", "Temperature (°C)", "Description", "Wind Speed (km/h)", "Humidity (%)", "Fetched At"]

    # Create a list to store processed data
    rows = []

    for filename in os.listdir(json_folder):
        if filename.endswith("_weather.json"):
            filepath = os.path.join(json_folder, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                data = json.load(file)
                location = data["location"]["name"]
                temperature = data["current"]["temperature"]
                description = ", ".join(data["current"]["weather_descriptions"])
                wind_speed = data["current"]["wind_speed"]
                humidity = data["current"]["humidity"]
                fetched_at = datetime.now().strftime("%Y-%m-%d %H:%M")

                # Clean special characters (if needed)
                location = location.encode("ascii", "ignore").decode("ascii")
                description = description.encode("ascii", "ignore").decode("ascii")

                rows.append([location, temperature, description, wind_speed, humidity, fetched_at])

    # Save to CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write header
        writer.writerows(rows)   # Write data rows

    print(f"Processed weather data saved to {csv_file}")

if __name__ == "__main__":
    process_weather_data("weather_data", "weather_data/processed_weather.csv")
