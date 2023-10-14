# Import packages
from dash import Dash, html, dcc
import pandas as pd

# Create a dataset by reading raw content from a github repo
# To get more info on this data go to: https://github.com/plotly/datasets/blob/master/Dash-Course/makeup-shades/README-shades.md
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Dash-Course/makeup-shades/shades.csv')

# Description of labels that will be used in radio buttons
labelName_list = ["Fenty Beauty's PRO FILT'R Foundation Only",
                  "Make Up For Ever's Ultra HD Foundation Only",
                  "US Best Sellers",
                  "BIPOC-recommended Brands with BIPOC Founders",
                  "BIPOC-recommended Brands with White Founders",
                  "Nigerian Best Sellers",
                  "Japanese Best Sellers",
                  "Indian Best Sellers"
                  ] 

# Create a list
dropDown_list = df['brand'].unique().tolist()

# Create a list to be used in radio buttons
radioButtons_list = [{"label" : name, "value" : index} for index, name in enumerate(labelName_list)]

# Create a variable for the dropDown
brandSelector = dcc.Dropdown(options = dropDown_list, value = dropDown_list[3])

# Create a variable for the radio buttons
radioButtons = dcc.RadioItems(options = radioButtons_list)

# Create the app object
app = Dash(__name__)

# Define the app layout
app.layout = html.Div([
    brandSelector,
    radioButtons
])

# Generate the dashboard
if __name__ == '__main__':
   app.run(debug = True,
           port  = 8050
           )