# ESPURR on Messenger

Espurr, now on Messenger! Fork from JARVIS-on-Messenger

[![Build Status](https://github.com/superbahbi/ESPURR-on-Messenger.svg?branch=master)](https://github.com/superbahbi/ESPURR-on-Messenger)


Messenger is now used by 900 million people every month. With the launch of Send / Receive API, bots are about to [take](http://time.com/4291214/facebook-messenger-bots/) [over](http://www.computerworld.com/article/3055588/social-media/an-army-of-chatbots-will-take-over-facebook-here-s-why.html).


### Sample Queries

`Hi, Espurr!`  
`Are you there?`  
`tell me a joke`  
`iron man movie`  
`define a superhero`  
`wiki html`  
`anything you want book`  
`random quote`  
`usd to eur rate`  
More examples can be found [here](https://github.com/swapagarwal/JARVIS-on-Messenger/tree/master/modules/tests).

### Local Development / Testing

1. Clone this repo.
2. `sudo apt-get install python-dev libffi-dev libssl-dev`
3. `pip install -r requirements.txt`
4. `python jarvis.py`
5. Visit the following URLs to see results:  
`http://localhost:5000/process/?q=<YOUR_QUERY>` returns the intent of the query.  
`http://localhost:5000/search/?q=<YOUR_QUERY>` returns the search result of the query.
