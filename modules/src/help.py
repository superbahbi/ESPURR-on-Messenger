from templates.text import TextTemplate
import facebook

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN', config.ACCESS_TOKEN)
def process(input, entities, sender):
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    profile = graph.get_object("%s" % (sender))
    name = profile['first_name'].split()
    help = '''Hi %s! I'm Espurr, your personal assistant.\nTell me things like the following:\n
  - define a superhero\n  - iron man 2 movie plot\n  - tell me a joke\n  - wiki html\n  - anything you want book\n  - random quote\n  - usd to eur rate\n
I'm always learning, so do come back and say hi from time to time!\nHave a nice day.''' % (name[0])
    output = {
        'input': input,
        'output': TextTemplate(help).get_message(),
        'success': True
    }
    return output
