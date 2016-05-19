import requests
import os
import config
import firebase
from templates.text import TextTemplate

FIREBASE_URL = os.environ.get('FIREBASE_URL', config.FIREBASE_URL)
def process(input, entities, sender):
    output = {}
    r = firebase.FirebaseApplication(FIREBASE_URL, None)
    result = r.get('/user', None)
    template = TextTemplate()
    print r
    print result
    res = 'Name: %s' % (result)
    try:
        output['input'] = input
        output['output'] = TextTemplate(res).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
