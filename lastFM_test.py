#Making API calls to lastFM music library.

import requests

#Defining our API key and user agent.
API_KEY = ''
USER_AGENT = 'rchriskoka'

"""
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
print(r.status_code)"""

#Using a function to execute the code above

def lastfm_get(payload):
	#define headers & URL
	headers = {'user-agent':'USER_AGENT'}
	url = 'http://ws.audioscrobbler.com/2.0/'
	
	#Add API key and format the payload
	payload['api_key'] = API_KEY
	payload['format'] = 'json'
	
	response = requests.get(url, headers = headers, params = payload)
	return response
	
#Now let's see how much it simplifies our earlier requests
r = lastfm_get({
	'method' : 'chart.gettopartists' })
	
print(r.status_code)
		

import json

def jprint(obj):
	#create a formatted string of the Python JSON object
	text = json.dumps(obj, sort_keys=True, indent=4)
	print(text)
	
jprint(r.json()['artists']['@attr'])
