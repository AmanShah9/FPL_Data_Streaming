from pip._vendor import requests
import json
from pprint import pprint


main_url = 'https://fantasy.premierleague.com/api/'

r = requests.get(main_url + 'bootstrap-static/').json()

pprint(r, indent=2, depth=1, compact=True)