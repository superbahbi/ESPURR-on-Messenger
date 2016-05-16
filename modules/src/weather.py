import requests
import os
import config
from templates.text import TextTemplate

OPENWEATHER_API = os.environ.get('OPENWEATHER_API', config.OPENWEATHER_API)
def process(input, entities, sender):
    output = {}
    try:
        location = entities['location'][0]['value']
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + OPENWEATHER_API + '&units=imperial')
        data = r.json()
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        wind = data['wind']['speed'];
        wind_direction = data['wind']['deg']
        humidity = data['main']['humidity']
        msg = "Oh %s! Right now it's %s.\nTemperature: %sF\nHumidity: %s%\nWind: %s mph" % (location, description, temp, humidity, wind)
 
        output['input'] = input
        output['output'] = TextTemplate(msg).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output