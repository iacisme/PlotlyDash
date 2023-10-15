# Import packages
from dash import Dash, html, dcc
import pandas as pd

# Create a dataset by reading raw content from a github repo
# To get more info on this data go to: https://github.com/plotly/datasets/blob/master/Dash-Course/makeup-shades/README-shades.md
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

# Create a list
dropDown_list = df['brand'].unique().tolist()

# Create a variable for the dropDown
brandSelector = dcc.Dropdown(options = dropDown_list, value = dropDown_list[3])

# Create the app object
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    brandSelector
])

# Generate the dashboard
if __name__ == '__main__':
   app.run(debug = True,
           port  = 8050
           )
