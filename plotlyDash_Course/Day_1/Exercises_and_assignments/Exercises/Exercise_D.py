# Import packages
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Create a dataset by reading raw content from a github repo
# To get more info on this data go to: https://github.com/plotly/datasets/blob/master/Dash-Course/makeup-shades/README-shades.md
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

# Labels that will be applied to the graph
scatterplotLabels = {
   "V" : "Value / Brightness",
   "S" : "Saturation"
}

# Create a graph figure
fig = px.scatter(df,
                 x = "V",
                 y = "S",
                 labels = scatterplotLabels,
                 title = "Scatterplot of Saturation vs Value/Brightness")

# Create the app object
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([dcc.Graph(figure = fig)])

# Generate the dashboard
if __name__ == '__main__':
   app.run(debug = True,
           port  = 8050
           )