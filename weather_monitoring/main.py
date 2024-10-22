# main.py
import time
import requests
# import schedule
from weather_api import WeatherAPI
from data_processor import process_weather_data, aggregate_daily_summary
from alerts import check_alerts
from database import create_database, save_to_database
from config import CITIES, INTERVAL, TEMP_THRESHOLD, OPENWEATHER_API_KEY
import pandas as pd


TEMP_THRESHOLD = 35  
#cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        return {
            'city': city,
            'date': pd.to_datetime('now').date(),
            'avg_temp': data['main']['temp'] - 273.15,  # Convert Kelvin to Celsius
            'max_temp': data['main'].get('temp_max', 0) - 273.15,  # Default to 0 if missing
            'min_temp': data['main'].get('temp_min', 0) - 273.15,  # Default to 0 if missing
            'humidity': data['main'].get('humidity', 0),  # Humidity percentage
            'wind_speed': data['wind'].get('speed', 0),  # Wind speed in m/s
            'dominant_condition': data['weather'][0].get('description', 'Unknown').title()
        }

    else:
        print(f"Failed to get data for {city}: {response.status_code}")
        return None

def main():
    create_database()  # Initialize database
    while True:
        weather_data_list = []

        for city in CITIES:  # Use CITIES from config
            weather_data = fetch_weather_data(city)
            #weather_data = fetch_weather_forecast(city)
            if weather_data:
                weather_data_list.append(weather_data)

        if weather_data_list:
            daily_summary = pd.DataFrame(weather_data_list)

            check_alerts(daily_summary, TEMP_THRESHOLD)

            save_to_database(daily_summary)

            print(daily_summary)

        time.sleep(INTERVAL)  # Use INTERVAL from config, defaulting to 300 seconds

if __name__ == "__main__":
    main()