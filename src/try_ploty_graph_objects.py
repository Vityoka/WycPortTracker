import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.data as sampleData

# Modifying existing plots created with plotly express
df_tips = sampleData.tips()
print(df_tips.head()) # Header is the following:  total_bill tip sex smoker day time size


df_countries = sampleData.gapminder()
print(df_countries.head()) # Header:  country continent  year  lifeExp  pop gdpPercap iso_alpha  iso_num
df_India = df_countries[df_countries['country']=='India']
print(df_India.head())

# Create plot using graph_objects
# graph_object doesnt have a line plot. It has scatter, bar, pie, etc.
# Scatter can be used to display lines
go_scatter = go.Scatter(x=df_India['year'], y=df_India['pop']) # This returns a Scatter object, not a figure like plotly express
# Therefore we need to create a figure too, and give the scatter object as the data parameter.
fig_scatter = go.Figure(data=go_scatter)
fig_scatter.show()

# We can do it in one constructor too
fig_scatter2 = go.Figure(
    # Data is the trace object instance of the figure object. 
    #Mode can set whether markers are connected or not, so line plot can be made.
    data=go.Scatter(x=df_India['year'], y=df_India['pop'], mode='lines') 
)

# Also we can modify the plots using the functions of the figure object. 
# The figure object itself has 3 main components (data, layout, frame): https://plotly.com/python/figure-structure/
fig_scatter2.add_hline(y=1e9) # Add a horizontal line at the 1B population
# The already existing layout can also be updated.
# The layout defines the title, legend, etc.
fig_scatter2.update_layout(title='Population of India')
fig_scatter2.show()

# We can also define how we want the scatter plot to look like. For example how the markers should look like.
fig_scatter3 = go.Figure(
    data=go.Scatter(x=df_India['year'], y=df_India['pop'],
                        mode='lines+markers',
                        line = dict(color='green'),
                        marker = dict(color='red', size=10, symbol='hexagram-dot',
                            line=dict(
                                color='MediumPurple',
                                width=2)
                        )
    )
)
fig_scatter3.show()
