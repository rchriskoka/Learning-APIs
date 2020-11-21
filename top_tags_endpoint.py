#In order to make our data more interesting, let's use another last_fm API endpoint to add some extra data about each artist.

import time
from lastFM_test import *
from IPython.core.display import clear_output

# Last.fm allows its users to create "tags" to categorize artists. 
# By using artist.getTopTags endpoint we can get the top tags from an individual artist.

def lookup_tags(artist):
	response = lastfm_get({
	'method' : 'artist.getTopTags',
	'artist' : 'artist'
	})
	
	# if there's an error, just return nothing.
	if response.status_code != 200:
		return None
	
	# extract the top three tags and turn them into a string
	tags = [t['name'] for t in response.json()['toptags']['tag'][:3]]
	tags_str = ', '.join(tags)
	
	# rate limiting
	if not getattr(response, 'from_cache', False):
		time.sleep(0.25)
	print(tags_str)
	
#Testing the function on an artist.
lookup_tags("Billie Eilish")

