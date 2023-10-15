# Import packages
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Create a dataset by reading raw content from a github repo
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv')

# Create a list that can be used for dropdowns
stateDropdown_list = df['state'].unique().tolist()

# Create a variable for the dropDown
stateSelector = dcc.Dropdown(options = stateDropdown_list, value = stateDropdown_list[0], id = "state-dropdown")

# Create the app object
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    stateSelector
])

# Generate the dashboard
if __name__ == '__main__':
   app.run(debug = True,
           port  = 8050
           )
