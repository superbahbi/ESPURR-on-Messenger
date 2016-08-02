import modules

def test_hello():
    assert('pokemon' == modules.process_query('notify')[0])
    assert('pokemon' != modules.process_query('something random')[0])
