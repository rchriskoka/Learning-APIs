#Exploring how to use APIs with query parameters.

#Still playing with the 'http://api.open-notify.org/iss-pass' on International Space Station


import requests
import json
from open_notify import jprint

'''An example of an API that requires us to specify and endpoint is http://api.open-notify.org/iss-pass.json
   Its documentation specifies require lat (latitude) and long (longitude) parameters. '''
   
#This endpoint tells us the next times that the International Space Station will pass over a given location on earth   

#Adding optional keyword argument params - Let's use Ghana's location :)
parameters = {
	"lat" : 7.9465,
	"lon" : 1.0232
}

#Making the requests using the above parameters & checking our response
response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)

print(response.status_code)
jprint(response.json())

''' Understanding The Pass Times.
A dictionary with three keys.
The third key, response, contains a list of pass times. 
Each pass time is a dictionary with risetime (pass start time) and duration keys '''

#Extracting pass times from our JSON object
pass_times = response.json()['response']
jprint(pass_times)

#Next, we'll use a loop to extract just the five risetime values

risetimes = []

for d in pass_times:
	time = d['risetime']
	risetimes.append(time)
	
print(risetimes)

#The given times are in a format known as timestam or epoch. 
#Let's use datetime.fromtimestamp() method to convert these into easier to understand times.

from datetime import datetime

times = []

for rt in risetimes:
	time = datetime.fromtimestamp(rt)
	times.append(time)
	print(time)
	
#PS: Looks like ISS passes over Ghana often!!! 



