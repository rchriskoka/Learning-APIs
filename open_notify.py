#Working with Open Notify API which gives access to data about the international space station.

import requests

#A request to know the who is at space currently.
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
print(response.json())

import json

#Demonstrating how to use the dumps function to print a formatted string which makes 
#it easier to understand the JSON output

def jprint(obj):
	#create a formatted string of the Python JSON object.
	text = json.dumps(obj, sort_keys=True, indent= 4)
	print(text)
	
jprint(response.json())
