import requests

API_KEY = '72db5080aa5578cb021a17006670a944'


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'main' in data and 'weather' in data:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            return {
                'temperature': temperature,
                'description': description,
                'icon': icon
            }
        else:
            return {'error': 'Invalid response format'}
    else:
        return {'error': 'Failed to fetch data from API'}


# Example usage:
weather_data = get_weather('London')
if 'error' in weather_data:
    print(weather_data['error'])
else:
    print(weather_data)
