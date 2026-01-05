from main import get_hot_or_cold, fetch_weather_data
import pytest


def test_get_hot_or_cold_hot():
    assert get_hot_or_cold(30) == "hot"
    assert get_hot_or_cold(26) == "hot"
    assert get_hot_or_cold(25) == "cold"
    assert get_hot_or_cold(0) == "cold"


def test_fetch_weather_data(mocker):
    # Mock the requests.get method
    mock_get = mocker.patch("main.requests.get")

    # Set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 22, "condition": "Sunny"}

    # Call function
    result = fetch_weather_data("London")

    # Assertions
    assert result == {"temperature": 22, "condition": "Sunny"}
    mock_get.assert_called_once_with("http://api.weatherapi.com/v1/London")
