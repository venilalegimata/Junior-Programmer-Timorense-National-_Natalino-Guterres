import requests
import time

# Your API key and endpoint (Replace with your API key)
# API_KEY = 'your_api_key'
API_URL = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"

def fetch_data():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            data = response.json()
            temperature = data['current']['temperature_2m']
            humidity = data['current']['wind_speed_10m']
            print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Run the fetch every 10 minutes
while True:
    fetch_data()
    time.sleep(600)  # 600 seconds = 10 minutes
