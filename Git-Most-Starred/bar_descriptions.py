import pygal 
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

"""Adding Custom tooltips. 
In pygal, hovering the cursor over an individual bar shows the information that the bar represents. This is commonly called a tooltip. 
Let's create a custom tooltip to show each project's description as well.
Let's look at a short example using the first three projects plotted individually with custom labels passed for each bar.
"""

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['public-apis', 'Python-100-Days', 'Python']

plot_dicts  = [
	{'value':114118, 'description': 'public-apis'},
	{'value':97058, 'description': 'Python-100-Days'},
	{'value':94714, 'description': 'Python'}
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')
