import requests
import os
import config
from firebase import firebase
from templates.text import TextTemplate

FIREBASE_URL = os.environ.get('FIREBASE_URL', config.FIREBASE_URL)
def process(input, entities, sender):
    output = {}
    try:
        r = firebase.FirebaseApplication(FIREBASE_URL, None)
        data ={'name': 'bahbi lee', 'id': sender,'created_at': datetime.datetime.now()}
        r.post('/users', data, {'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})
        #result = r.get('/user', None)
        res = 'Name: %s' % (sender)
        output['input'] = input
        output['output'] = TextTemplate(res).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
