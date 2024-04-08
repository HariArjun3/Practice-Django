import requests


API_KEY = '72db5080aa5578cb021a17006670a944'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    return temperature, description


print(get_weather('London'))
