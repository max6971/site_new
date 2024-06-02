import requests

import pprint

parms ={ 'q': 'html'}
respons = requests.get('https://api.github.com', params=parms)

respons_json = respons.json()

pprint.pprint(respons_json)