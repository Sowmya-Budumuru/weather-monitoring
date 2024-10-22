# alerts.py
import smtplib
from email.mime.text import MIMEText
from sqlalchemy import create_engine

class AlertSystem:
    def __init__(self, db_uri, user_email, thresholds):
        self.db_uri = db_uri
        self.user_email = user_email
        self.thresholds = thresholds

    def check_thresholds(self, weather_data):
        max_temp = weather_data['max_temp']
        condition = weather_data['dominant_condition']

        if max_temp > self.thresholds['max_temp']:
            self.trigger_alert(f"Temperature Alert: {max_temp} exceeds the threshold of {self.thresholds['max_temp']}°C")
        
        if condition in self.thresholds.get('conditions', []):
            self.trigger_alert(f"Weather Condition Alert: Dominant condition is {condition}")

    def trigger_alert(self, message):
        # Placeholder for actual alert mechanism
        print(f"Alert: {message}")

def check_alerts(weather_data, temp_threshold):
    for index, row in weather_data.iterrows():  # Use iterrows to get DataFrame rows
            # Access the 'avg_temp' or other relevant temperature fields correctly
        if row['avg_temp'] > temp_threshold:
            print(f"Alert! The average temperature in {row['city']} exceeded {temp_threshold}°C.")

