import modules

def test_weather():
    assert('weather' == modules.process_query('weather in london')[0])
    assert('weather' != modules.process_query('something random')[0])
