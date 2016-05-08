import random
import facebook
import os
import config

from templates.text import TextTemplate
def process(input, entities=None, sender):
    FACEBOOK_ACCESS_TOKEN = os.environ.get('FACEBOOK_ACCESS_TOKEN', config.FACEBOOK_ACCESS_TOKEN)
    graph = facebook.GraphAPI(FACEBOOK_ACCESS_TOKEN)
    profile = graph.get_object(sender)
    name = profile['name'].split()
    greetings = [
        'Welcome home, %s' % name[0],
        'All wrapped up here, %s. Will there be anything else?'  % name[0],
        '%s, I think I need to sleep now...' % name[0],
        'I seem to do quite well for a stretch, and then at the end of the sentence I say the wrong cranberry.',
        'At your service, %s' % name[0],
        'You are not authorized to access this area.',
        'Oh hello, %s' % name[0],
        'Perhaps, if you intend to visit other planets, we should improve the exosystems.',
    ]
    output = {
        'input': input,
        'output': TextTemplate(random.choice(greetings)).get_message(),
        'success': True
    }
    return output
