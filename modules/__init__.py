import config
import os
import requests
import sys
from src import *
from chatterbot import ChatBot
from templates.text import TextTemplate

WIT_AI_ACCESS_TOKEN = os.environ.get('WIT_AI_ACCESS_TOKEN', config.WIT_AI_ACCESS_TOKEN)

def process_query(input):
    try:
        r = requests.get('https://api.wit.ai/message?v=20160511&q=' + input, headers={
            'Authorization': 'Bearer %s' % WIT_AI_ACCESS_TOKEN
        })
        data = r.json()
        intent = data['outcomes'][0]['intent']
        entities = data['outcomes'][0]['entities']
        confidence = data['outcomes'][0]['confidence']
        if intent in src.__all__ and confidence > 0.5:
            return intent, entities
        else:
            return None, {}
    except:
        return None, {}

def search(input, sender):
    chatbot = ChatBot("Espurr")
    chatbot.train("chatterbot.corpus.english")
    intent, entities = process_query(input)
    if intent is not None:
        data = sys.modules['modules.src.' + intent].process(input, entities, sender)
        if data['success']:
            return data['output']
        else:

            return TextTemplate(chatbot.get_response("Hello, how are you today?")).get_message()
    else:
        return TextTemplate('I\'m sorry; I\'m not sure I understand what you\'re trying to say sir.\nTry typing "help" or "request"').get_message()
