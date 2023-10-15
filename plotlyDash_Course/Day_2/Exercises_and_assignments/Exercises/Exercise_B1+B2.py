# Import packages
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# Create a dataset by reading raw content from a github repo
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/US-Exports/2011_us_ag_exports.csv')

# Create a list of features
featureNames = df.columns.to_list()

# Create a list that can be used for dropdowns
stateDropdown_list = df['state'].unique().tolist()

# Dashboard Header
html_dashboardTitle = html.Div(id = 'my-title', children = "Us Agricultural Exports in 2011 - By State")

# Create a variable for the dropDown
stateSelector = dcc.Dropdown(options = stateDropdown_list, value = stateDropdown_list[0], id = "state-dropdown")

exportGraph = dcc.Graph(id = "graph1")

# Create the app object
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    html_dashboardTitle,
    stateSelector,
    exportGraph
])

@app.callback(
   Output(component_id = "graph1", component_property = "figure"),
   Input(component_id = "state-dropdown", component_property = "value")
   )
def update_graph(state_selected):
   
   df_country = df[df['state'] == state_selected]
   
   fig = px.bar(df_country,
                x = "state",
                y = [featureNames[4], featureNames[5], featureNames[8]],
                )
   
   return fig

# Generate the dashboard
if __name__ == '__main__':
   app.run(debug = True,
           port  = 8050
           )