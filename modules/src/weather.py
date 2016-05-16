import requests
import os
import config
from templates.text import TextTemplate

OPENWEATHER_API = os.environ.get('OPENWEATHER_API', config.OPENWEATHER_API)
def process(input, entities, sender):
    output = {}
    try:
        location = entities['location'][0]['value']
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + OPENWEATHER_API)
        data = r.json()
        print data
        temp = data['main']['temp']
 
        output['input'] = input
        output['output'] = TextTemplate(temp).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
