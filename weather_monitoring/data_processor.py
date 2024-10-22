# data_processor.py
import pandas as pd
from datetime import datetime

def convert_temperature(value, from_unit='kelvin', to_unit='celsius'):
    if from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
    elif from_unit == 'celsius':
        if to_unit == 'kelvin':
            return value + 273.15
        elif to_unit == 'fahrenheit':
            return (value * 9/5) + 32
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    return value  

def process_weather_data(data):
    main = data['main']
    weather = data['weather'][0]
    return {
        'city': data['name'],
        'temperature': convert_kelvin_to_celsius(main['temp']),
        'feels_like': convert_kelvin_to_celsius(main['feels_like']),
        'condition': weather['main'],
        'timestamp': datetime.fromtimestamp(data['dt'])
    }

def aggregate_daily_summary(weather_data):
    df = pd.DataFrame(weather_data)
    daily_summary = df.groupby(df['timestamp'].dt.date).agg({
        'temperature': ['mean', 'max', 'min'],
        'condition': lambda x: x.mode()[0]  # dominant weather condition
    }).reset_index()
    daily_summary.columns = ['date', 'avg_temp', 'max_temp', 'min_temp', 'dominant_condition']
    return daily_summary

