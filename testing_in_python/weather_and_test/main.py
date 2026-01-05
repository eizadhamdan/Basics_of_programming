import requests


def get_hot_or_cold(temperature):
    """
    Determines if the temperature is considered 'hot' or 'cold'.

    Parameters:
    temperature_celsius (float): The temperature in degrees Celsius.

    Returns:
    str: 'hot' if temperature is above 25 degrees Celsius, 'cold' otherwise.
    """
    if temperature > 25:
        return "hot"
    else:
        return "cold"


def fetch_weather_data(city):
    """
    Fetches weather data for a given city.

    Parameters:
    city (str): The name of the city.

    Returns:
    dict: A dictionary containing weather information.
    """
    response = requests.get(f"http://api.weatherapi.com/v1/{city}")
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError("Could not fetch weather data")
