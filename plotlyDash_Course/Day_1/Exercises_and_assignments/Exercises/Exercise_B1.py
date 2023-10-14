# Import packages
from dash import Dash, html, dcc
import dash_ag_grid as dag
import pandas as pd

# Create a dataset by reading raw content from a github repo
# To get more info on this data go to: https://github.com/plotly/datasets/blob/master/Dash-Course/makeup-shades/README-shades.md
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

# Create column definitions that will be used by ag_grid
column_list = [{'field' : columnName} for columnName in df.columns]

# Create a grid for the data
grid = dag.AgGrid(
    id = "get-started-example-basic",
    rowData = df.to_dict("records"),
    columnDefs = column_list
)

# Create the app object
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([grid])

# Generate the dashboard
if __name__ == '__main__':
   app.run(debug = True,
           port  = 8050
           )
