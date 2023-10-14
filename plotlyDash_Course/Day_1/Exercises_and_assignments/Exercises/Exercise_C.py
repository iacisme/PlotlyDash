# Import packages
from dash import Dash, html, dcc
import pandas as pd

# Create a dataset by reading raw content from a github repo
# To get more info on this data go to: https://github.com/plotly/datasets/blob/master/Dash-Course/makeup-shades/README-shades.md
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

# Create a list of dataset features to be used in dcc
column_list = df.columns

# Create a slider component
feature_slider = dcc.Slider(0, len(column_list)-1, marks = {idx: feature for idx, feature in enumerate(column_list)}, value = 5)

# Create a checklist component
feature_checklist =   dcc.Checklist(column_list)

# Create the app object
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([feature_slider, feature_checklist])

# Generate the dashboard
if __name__ == '__main__':
   app.run(debug = True,
           port  = 8050
           )