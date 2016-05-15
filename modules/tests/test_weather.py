import modules

def test_weather():
    assert('request' == modules.process_query('weather in london')[0])
    assert('request' != modules.process_query('something random')[0])
