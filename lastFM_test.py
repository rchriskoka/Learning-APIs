#Making API calls to lastFM music library.

import requests

#Defining our API key and user agent.
API_KEY = ''
USER_AGENT = 'kookies'

#Creating a dictionary for our headers and parameters and making our first request.
headers = { 
	'user-agent' : USER_AGENT
}

payload = {
	'api_key' : API_KEY,
	'method' : 'chart.gettopartists',
	'format' : 'json'
}

r = requests.get('http://ws.audioscrobbler.com/2.0/', headers = headers, params = payload)
print(r.status_code)
