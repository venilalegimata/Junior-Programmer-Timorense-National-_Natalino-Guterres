import requests
import time

API_URL = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
response = requests.get(API_URL)
data = response.json()
temperature = data['current']['temperature_2m']
humidity = data['current']['wind_speed_10m']

def calculate_heat_index(temperature, humidity):
    # Convert Celsius to Fahrenheit if needed
    T = temperature
    R = humidity

    # Heat index formula
    HI = (-42.379 + 2.04901523 * T + 10.14333127 * R - 0.22475541 * T * R 
          - 0.00683783 * T ** 2 - 0.05481717 * R ** 2 + 0.00122874 * T ** 2 * R 
          + 0.00085282 * T * R ** 2 - 0.00000199 * T ** 2 * R ** 2)

    # Adjustments for specific conditions
    if R < 13 and 80 <= T <= 112:
        adj = ((13 - R) / 4) * ((17 - abs(T - 95)) / 17) ** 0.5
        HI -= adj
    elif R > 85 and 80 <= T <= 87:
        adj = ((R - 85) / 10) * ((87 - T) / 5)
        HI += adj

    return HI

# Example usage
temperature_f = temperature  # Example temperature in Fahrenheit
humidity = humidity       # Example humidity in percentage
heat_index = calculate_heat_index(temperature_f, humidity)

print(f"Heat Index: {heat_index:.2f}°F")
