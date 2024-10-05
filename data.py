import os
import requests
import pandas as pd
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set the API key directly (for testing purposes)
API_KEY = '4beed707e83d4decbcb141001240510'  # Replace with your WeatherAPI key
CITY = os.getenv('WEATHER_CITY', 'Hyderabad')  # Default to Hyderabad if not set
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

def fetch_weather_data(city):
    """Fetch weather data for a given city from WeatherAPI."""
    try:
        response = requests.get(BASE_URL, params={'key': API_KEY, 'q': city, 'aqi': 'no'})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'temperature': data['current']['temp_c'],  # Temperature in Celsius
            'humidity': data['current']['humidity'],
            'pressure': data['current']['pressure_mb'],  # Pressure in hPa
            'weather': data['current']['condition']['text']
        }
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred for city {city}: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred for city {city}: {err}")
    return None

def save_to_csv(weather_data):
    """Save weather data to a CSV file."""
    if weather_data:
        try:
            df = pd.DataFrame([weather_data])
            df.to_csv('weather_data.csv', mode='a', header=not os.path.exists('weather_data.csv'), index=False)
            logging.info("Weather data saved to weather_data.csv")
        except Exception as e:
            logging.error(f"Failed to save data to CSV: {e}")

def main():
    """Main function to execute the program."""
    weather_data = fetch_weather_data(CITY)
    save_to_csv(weather_data)

if __name__ == '__main__':
    main()
