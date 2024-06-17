from config import open_weather_token
import requests
from pprint import pprint
from datetime import datetime


def get_weather(city, open_weather_token):

    code_to_weather = {
        'Clear': 'Clear \U00002600',
        'Clouds': 'Clouds \U00002601',
        'Rain': 'Rain \U00002614',
        'Drizzle': 'Drizzle \U00002614',
        'Thunderstorm': 'Thunderstorm \U000026A1',
        'Snow': 'Snow \U0001F328',
        'Mist': 'Mist \U0001F32B'
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        #pprint(data)

        city = data['name']
        cur_weather = data['main']['temp']

        weather_description = data['weather'][0]['main']
        if weather_description in code_to_weather:
            wd = code_to_weather[weather_description]
        else:
            wd = f'Look in to window, jerk...'

        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.fromtimestamp(data['sys']['sunset'])
        length_day = sunset - sunrise
        print(
            f'***{datetime.now().strftime("%Y-%m-%d %H:%m")}***\n'
            f'Weather in the {city}\nTemperature: {cur_weather} C° {wd}\n'
            f'Humidity: {humidity} %\nPressure: {pressure} mm\n'
            f'Wind: {wind} m/s \nSunrise: {sunrise}\nSunset: {sunset}\n'
            f'Length of the day: {length_day}\n'
        )

    except Exception as ex:
        print(ex)
        print('Try again later...')


def main():
    city = input('Input city name: ')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
