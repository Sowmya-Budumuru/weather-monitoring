# weather_summary.py
import pandas as pd
#from sqlalchemy import create_engine

def calculate_daily_summary(weather_data):
    summary = {
        'avg_temp': weather_data['avg_temp'].mean(),
        'max_temp': weather_data['max_temp'].max(),
        'min_temp': weather_data['min_temp'].min(),
        'avg_humidity': weather_data['humidity'].mean(),
        'max_wind_speed': weather_data['wind_speed'].max(),
        'dominant_condition': weather_data['dominant_condition'].mode()[0],
    }
    return summary