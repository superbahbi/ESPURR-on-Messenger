import random
import os
from templates.text import TextTemplate

def process(input, entities, sender):
    
    greetings = [
        'Welcome home, %s' % sender,
        'All wrapped up here, %s. Will there be anything else?'  % sender,
        '%s, I think I need to sleep now...' % sender,
        'I seem to do quite well for a stretch, and then at the end of the sentence I say the wrong cranberry.',
        'At your service, %s' % sender,
        'You are not authorized to access this area.',
        'Oh hello, %s' % sender,
        'Perhaps, if you intend to visit other planets, we should improve the exosystems.',
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(greetings)).get_message(),
        'success': True
    }
    return output