#Looking at the most starred javascript projects on git.


import requests

#making API call
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
response = requests.get(url)
print(response.status_code)

#Store response in a variable.
response_dict = response.json()

#Working with results.
print(response_dict.keys())
print("Total repositories: ", response_dict['total_count'])

#Explore info about the repositories.
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

#Visualizing repos using pygal

import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

names, plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	
	plot_dict = {
		'value' : repo_dict['stargazers_count'],
		'label' : repo_dict['description'] or "",
		'xlink' : repo_dict['html_url'], #Adding a link to the project
		}
	plot_dicts.append(plot_dict)
	
#Make visualization
my_style = LS('#443345' , base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred JavaScript Projects On Github'
chart.x_labes = names

chart.add("", plot_dicts)
chart.render_to_file('js_repos.svg')
