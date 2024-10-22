# Real-Time Weather Monitoring Application

## Overview
The Real-Time Weather Monitoring Application is designed to gather, process, and analyze weather data for metropolitan cities in India, utilizing the OpenWeatherMap API. It provides summarized weather insights through daily rollups and aggregates, including visualizations and alerting capabilities. The system is intended to help users stay informed about weather conditions and receive timely notifications for critical weather events.

## Project Structure
The project is organized as follows:

weather-monitoring-app/  
├── app.py                       # Main entry point for running the application  
├── config.py                  # Configuration settings for the application  
├── database.py                # Database connection and ORM models  
├── data_processor.py          # Functions for data processing and aggregation  
├── fetch_data.py              # Script for fetching weather data from OpenWeatherMap  
├── alerting.py                # Module for the alerting system  
├── visualizations.py          # Code for generating visualizations  
├── save_daily_summary.py      # Code for saving daily summaries to the database  
├── daily_summary.py           # Logic for creating daily weather summaries  
├── requirements.txt           # List of dependencies  
├── .env                       # Environment variables (not included in version control  
└── README.md                  # Project documentation  

## Features
**Real** -Time Weather Data Collection: Fetches weather data from the OpenWeatherMap API for various metro cities in India.  
**Data Summarization** : Daily weather data rollups and aggregated summaries for metrics such as temperature, humidity, wind speed, and precipitation.  
**Alerting System** : Configurable thresholds for sending alerts based on specific weather conditions (e.g., temperature exceeding 40°C).  
**Data Visualization** : Graphical representation of weather trends over time, including temperature changes, humidity levels, and other key metrics.  
**Database Storage** : Stores collected and processed data in an SQLite database for persistence and historical analysis.  
**Scalability** : Designed with a modular architecture to facilitate the addition of more cities and other data sources.  

## Prerequisites
Before we begin, ensure you have met the following requirements:  

Python 3.8 or above installed
An API key for [OpenWeatherMap] (register at https://home.openweathermap.org/users/sign_up)
SQLite (installed by default with Python)
pip for managing Python packages

## Installation
Clone the Repository:  
git clone https://github.com/yourusername/weather-monitoring-app.git  
cd weather-monitoring-app

## Install Dependencies

Install the required Python libraries listed in requirements.txt:    
pip install -r requirements.txt  
Set Up Environment Variables  

**Create a .env file in the root directory and add your OpenWeatherMap API key**:  
OPENWEATHERMAP_API_KEY=your_api_key_here

## Usage
1.**Run the Application** : Start the application by running:    
python app.py

2.**Fetching Weather Data** : The application will automatically fetch weather data from OpenWeatherMap for the configured cities at specified intervals.

3.**Viewing Daily Summaries** : Daily weather summaries are saved to the database and can be queried for insights.

4.**Alerting** : When weather conditions exceed specified thresholds, alerts are generated. You can configure the alert delivery method (e.g., email, SMS, or in-app notification).

5.**Data Visualization** : Use visualizations.py to generate graphs that show trends in weather data. This module supports generating line charts for temperature, humidity, and other metrics.

## Database Schema
The application uses an SQLite database with the following schema:

1.**WeatherSummary** : Stores daily weather summaries, including city name, date, temperature, humidity, wind speed, and precipitation.  
2.**Alerts** : Logs alerts triggered by weather conditions exceeding thresholds.
      The WeatherSummary class is defined in database.py, which includes ORM models for creating and accessing database tables.

## Deployment
To deploy the application on a server, you can use the following approaches:  

1.**Docker** : Create a Dockerfile to containerize the application for easy deployment.  
2.**Cloud Services** : Deploy the application using cloud platforms such as AWS, Google Cloud, or Azure.  
3.**Scheduled Task** : Use a cron job or scheduled task to run the application at regular intervals.  

## Development
**Adding a New City** :
To add a new city, update the CITIES list in config.py:  

CITIES.append("New City")

**Extending the Alerting System**:
To add new alert conditions, modify the ALERT_THRESHOLD dictionary in config.py and update the check_alerts function in alerting.py to handle the new conditions.

**Testing**
To run tests, ensure you have the pytest library installed and execute:  

pytest  
Test cases cover key functionalities, such as data fetching, summarization, and alerting.

## Future Enhancements
**Support for Additional Data Sources** : Integrate other weather data providers for improved accuracy.  
**Machine Learning** : Use predictive models for forecasting weather trends.  
**Mobile App Integration** : Provide real-time weather updates via a mobile application.  
**Advanced Visualizations** : Implement dashboards using libraries like Plotly or Dash for more interactive insights.  
