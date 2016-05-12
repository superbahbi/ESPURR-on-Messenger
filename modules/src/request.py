from templates.button import ButtonTemplate

def process(input, entities, sender):
    request = '''Kindly click the following button to:\n
  - Request a new feature, by including some sample queries and their expected results.\n
  - Report a bug (I couldn't handle the query and/or gave unexpected results), by including your search query and the expected result.'''
    template = ButtonTemplate(request)
    template.add_web_url('Request / Report', 'http://bahbi.net')
    output = {
        'input': input,
        'output': template.get_message(),
        'success': True
    }
    return output
