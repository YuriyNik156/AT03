import pytest
from main import get_weather

def test_get_weather(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather' : [{'description': 'clear sky'}],
        'main' : {'temp' : 273.15}
    }

    api_key = '13e2e91ca5585170bfc25294bde29a16'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == {
        'weather' : [{'description': 'clear sky'}],
        'main' : {'temp' : 273.15}
    }

def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    api_key = '13e2e91ca5585170bfc25294bde29a16'
    city = 'London'

    weather_data = get_weather(api_key, city)

    assert weather_data == None
