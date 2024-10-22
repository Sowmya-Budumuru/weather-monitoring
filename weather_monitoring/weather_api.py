# weather_api.py
import requests
from config import OPENWEATHER_API_KEY

class WeatherAPI:
    def __init__(self, api_key, base_url="http://api.openweathermap.org/data/2.5/weather"):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_weather(self, city):
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Use metric for temperature in Celsius
            }
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)

            data = response.json()
            if 'main' not in data or 'weather' not in data:
                raise ValueError("Incomplete weather data received from API")

            return data

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError:
            print("Connection error. Please check your network.")
        except requests.exceptions.Timeout:
            print("Request timed out. Try again later.")
        except ValueError as ve:
            print(f"Data parsing error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return None


