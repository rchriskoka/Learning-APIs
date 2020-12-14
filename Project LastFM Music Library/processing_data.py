#In this example, we will look at processing data we retrieve from API requests
import pandas as pd
from rate_limiting import *

r0 = responses[0]
r0_json = r0.json()
r0_artists = r0_json['artists']['artist']
r0_df = pd.DataFrame(r0_artists)
r0_df.head()
