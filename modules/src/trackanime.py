import requests
import os
import config
from firebase import firebase
from templates.text import TextTemplate

FIREBASE_URL = os.environ.get('FIREBASE_URL', config.FIREBASE_URL)
def process(input, entities, sender):
    output = {}
    try:
        title = entities['search_query'][0]['value']
        r = firebase.FirebaseApplication(FIREBASE_URL, None)
        data = {'id': sender, 'title': title}
        r.post('/users', data)
        res = 'Added %s to you list' % (title)
        output['input'] = input
        output['output'] = TextTemplate(res).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
