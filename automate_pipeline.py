import fetch_data
import process_data
import generate_report

def main():
    print("Starting the weather data pipeline...")
    
    # Input locations
    locations = input("Enter locations separated by commas (e.g., Accra, Lagos, Nairobi): ").strip()
    if not locations:
        print("No locations provided. Exiting pipeline.")
        return
    locations = [loc.strip() for loc in locations.split(",")]

    # Fetch weather data
    print("Fetching weather data...")
    for location in locations:
        weather_data = fetch_data.fetch_weather(location)
        if weather_data:
            filename = f"{location.lower().replace(' ', '_')}_weather.json"
            fetch_data.save_weather_data(weather_data, location)

    # Process weather data
    print("Processing weather data...")
    processed_csv = "weather_data/processed_weather.csv"  # Specify the output CSV file path
    process_data.process_weather_data("weather_data", processed_csv)  # Provide both arguments

    # Generate report
    print("Generating reports...")
    generate_report.generate_report(processed_csv, 
                                    "weather_data/statistic_report.txt", 
                                    "weather_data/weather_report.xlsx", 
                                    "weather_data/visualize_report.png", 
                                    "weather_data/weather_report_interactive.html")  # Added the missing argument

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
