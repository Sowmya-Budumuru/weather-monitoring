# visualizer.py
import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine

class WeatherVisualizer:
    def __init__(self, db_uri):
        self.engine = create_engine(db_uri)

    def plot_daily_summary(daily_summary):
        plt.figure(figsize=(12, 6))
        plt.plot(daily_summary['date'], daily_summary['avg_temp'], label='Average Temperature')
        plt.plot(daily_summary['date'], daily_summary['max_temp'], label='Max Temperature')
        plt.plot(daily_summary['date'], daily_summary['min_temp'], label='Min Temperature')
        plt.title('Daily Weather Summary')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.grid()
        plt.show()

