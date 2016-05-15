import requests
from templates.text import TextTemplate

def process(input, entities, sender):
    output = {}
    OPENWEATHER_API = os.environ.get('OPENWEATHER_API', config.OPENWEATHER_API)
    try:
        location = entities['location'][0]['value']
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + location + '&appid=' + OPENWEATHER_API)
        data = r.json()
        temp = data['main']['temp']
 
        output['input'] = input
        output['output'] = TextTemplate(temp).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
