import requests
import os
import config
from firebase import firebase
from templates.text import TextTemplate

FIREBASE_URL = os.environ.get('FIREBASE_URL', config.FIREBASE_URL)
def process(input, entities, sender):
    output = {}
    try:
        firebase = firebase.FirebaseApplication(FIREBASE_URL, None)
        result = firebase.get('/user', None)
        template = TextTemplate()
        print firebase
        print result
        res = 'Name: %s' % (result)
        
        output['input'] = input
        output['output'] = TextTemplate(res).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
