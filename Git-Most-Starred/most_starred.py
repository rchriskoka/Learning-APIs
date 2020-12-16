#The goal of this project is to use GitHub's API request information about python projects on the site and then generate an interactive visualization
# of the relative popularity of these projects


#We begin by issuing an API call and processing the results by identifying the most starred Python projects on Github
import requests

#Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print("Status Code: ", response.status_code)

#Store API response in a variable
response_dict = response.json()

#Working with the response dictionary - let's get to work on the data retrieved and stored from our API call
print(response_dict.keys())
print("Total repositories: ", response_dict['total_count'])

#Explore information about the repositories
repo_dicts = response_dict['items']
print("Repositories returned: ", len(repo_dicts))

#Let's examine the first repository
repo_dict = repo_dicts[0]
"""print("\nKeys:" , len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key) """
	

#Pulling out selected information about the first repository
"""
print("\nSelection Information About First Repository:" )
print('Name: ', repo_dict['name'])
print('Owner: ', repo_dict['owner']['login'])
print('Stars: ', repo_dict['stargazers_count'])
print('Repository: ', repo_dict['html_url'])
print('Created: ', repo_dict['created_at'])
print('Updated: ', repo_dict['updated_at'])
print('Description: ', repo_dict['description']) """


#Selected information about each repository
"""for repo_dict in repo_dicts:	
	print('\nName: ', repo_dict['name'])
	print('Owner: ', repo_dict['owner']['login'])
	print('Stars: ', repo_dict['stargazers_count'])
	print('Repository: ', repo_dict['html_url'])
	print('Description: ', repo_dict['description']) """
	

#Visualizing repositories using pygal. 
import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

names, plot_dicts = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	
	plot_dict = {
		'value': repo_dict['stargazers_count'],
		'label': repo_dict['description'] or "",
		'xlink': repo_dict['html_url'],  #Adding a clickable link to the project
		}
	plot_dicts.append(plot_dict)
	
#Make visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file('python_repos_.svg')


