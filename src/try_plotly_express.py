import pandas as pd
import plotly.express as px
import plotly.data as sampleData

# Graph_object is the low level interface of plotly.
# Plotly Express is the high level interface of plotly. It returns a Figure class which is a graph_object.Figure.
# Therefore any function calls on the figure uses the low-level interface.
# https://plotly.com/python/creating-and-updating-figures/

### PLOTLY EXPRESS HAS TO FUNCTIONS (line and scatter)

### USING PLOTLY EXPRESS LINE

df_countries = sampleData.gapminder()
print(df_countries.head())
# Header:  country continent  year  lifeExp  pop gdpPercap iso_alpha  iso_num

chosen_countries = (df_countries['country'] == 'China') | (df_countries['country'] == 'India')

# Create new database based on original filtered on one specific country
df_ChinaIndia = df_countries[chosen_countries]
print(df_ChinaIndia.head())

df_India = df_ChinaIndia[df_ChinaIndia['country']=='India']

# You can add x-y labels as a dictionary, add title, set data markers as true, add text for each marker
fig_line = px.line(df_India, x='year', y='pop', title="Population of India", markers=True, text='year')
fig_line.update_traces(textposition='bottom right') # Update previously set text to be placed to bottom right from the markers. Uses low-level API.
fig_line.show()

# Further arguments can alter the plot. E.g size or color can be chosen, which will alter the plotted scatter data
# depending on the given argument.
fig_line = px.line(df_ChinaIndia, x='year', y='pop', color='country')
fig_line.update_layout(xaxis_title="Year", yaxis_title="Population") # Update axis labels after using express. Use low level API
fig_line.show()

### USING PLOTLY EXPRESS SCATTER

df_tips = sampleData.tips()
print(df_tips.head())
# Header is the following:  total_bill tip sex smoker day time size

# basic scatter plot
fig1_scatter = px.scatter(df_tips, x='total_bill', y='tip')
fig1_scatter.show()

# Further arguments can alter the plot. E.g size or color can be chosen, which will alter the plotted scatter data
# depending on the given argument. This case, it will color the scattered data depending on the sex of the tipper,
# and modify the size of the plotted dot depending on the size of the tipping table from the database.
# The exact coloring and size cant be chosen as far as I understand
fig2_scatter = px.scatter(df_tips, x='total_bill', y='tip', size='size', color='sex')
fig2_scatter.show()

# functions for the figure can alter the appearance, but it can also override previous chosen appearance see below.
fig3_scatter = px.scatter(df_tips, x='total_bill', y='tip', size='size', color='sex')
fig3_scatter.update_traces(marker_size=10) # This will override the size set by the size='size argument, therefore we wont see the table sizes in the dots. Uses low-level API.
fig3_scatter.show()

# Faceting: Make subplots very very easy if task is trivial with faceting. If more complicated is needed than sublots shall be used.
fig4_scatter_facet = px.scatter(df_tips, x='total_bill', y='tip', color='sex', facet_col='smoker')
fig4_scatter_facet.show()

