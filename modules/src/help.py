from templates.text import TextTemplate
import facebook
import os
import config

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
def process(input, entities, sender):
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    profile = graph.get_object("%s" % (sender))
    name = profile['first_name'].split()
    help = '''Hi %s! I'm Espurr, your espuur ID is %s \n
I'm always learning, so do come back and say hi from time to time!\nHave a nice day.''' % (name[0], sender)
    output = {
        'input': input,
        'output': TextTemplate(help).get_message(),
        'success': True
    }
    return output
