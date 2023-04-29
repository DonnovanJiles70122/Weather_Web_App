import requests
from dotenv import load_dotenv
import os
from WeatherData import WeatherData

load_dotenv()
api_key = "Your API Key"


def get_lat_lon(city_name, state_code, country_code, API_key):
    response = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}'
    ).json()

    location_data = response[0]
    latitude, longitude = location_data.get('lat'), location_data.get('lon')

    return latitude, longitude

def get_current_weather(latitude, longitude, API_KEY):
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=imperial'
        ).json()
    weather_data = WeatherData(
        main=response.get('weather')[0].get('main'),
        description=response.get('weather')[0].get('description'),
        icon=response.get('weather')[0].get('icon'),
        temp=response.get('main').get('temp')
    )

    return weather_data

def get_weather_data(city_name, state_name, country_name):
    latitude, longitude = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(latitude, longitude, api_key)
    return weather_data

if __name__=='__main__':
    latitude, longitude = get_lat_lon('New Orleans', 'LA', 'America', api_key)
    print(get_current_weather(latitude, longitude, api_key))