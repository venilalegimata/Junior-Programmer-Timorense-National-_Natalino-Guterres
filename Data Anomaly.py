from requests.exceptions import ConnectionError, Timeout, HTTPError
import requests
import time

API_URL = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

# Function to fetch weather data with error handling
def fetch_weather_data():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Validate if temperature and humidity data are available and valid
        if 'current' in data:
            temperature = data['current'].get('temperature')
            humidity = data['current'].get('humidity')

            if temperature is None or humidity is None:
                print("Data anomaly: Missing temperature or humidity in the response")
                return
        else:
            print("Data anomaly: 'current' weather data not found in API response")

    except requests.exceptions.Timeout:
        print("Error: The request timed out")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the fetch every 10 minutes with error handling
while True:
    fetch_weather_data()
    time.sleep(600)  # 600 seconds = 10 minutes
