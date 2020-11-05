#Learning about rate limiting which is about using code to limit the number of times per second that we hit a particular API.
# Rate Limiting will make your code slower but it's better than getting banned from using an API altogether.

# The easiest way to perform rate limiting is to use Python's time.sleep() function.

import time
from lastFM_test import lastfm_get
from IPython.core.display import clear_output

responses = []

page = 1
total_pages = 99999 # this is just a dummy number so the loop starts

while page <= total_pages:
	payload = { 
		'method' : 'chart.gettoparists',
		'limit' : 500,
		'page' : page
	}

# print some output so we can see the status
print("Requesting page {}/{}".format(page,total_pages))
# clear the output to make things neater
clear_output(wait = True)

# make the API call
response = lastfm_get(payload)

# if we get an error, print the response and halt the loop.
if response.status_code !=200:
	print(response.text)
	
	
# extract pagination info
page = int(response.json()['artisits']['@attr']['page'])
total_pages = int(response.json()['artists']['@attr']['totalPages'])

# append response
responses.append(response)

#if it's not a cached result, sleep.
if not getattr(response, 'from_cache', False):
	time.sleep(0.25)
	
# increment the page number
page += 1
