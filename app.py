#import libraries
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Create a dash application
app = Dash(__name__)

# Total sales by Item Name
#tree_data = df.groupby(['Major Category', 'Item Name'])['Net Sales'].mean().reset_index()
# Item Quantity count
#bar_data = df.groupby(['Major Category', 'Item Name'])['Net Sales'].mean().reset_index()
# Percentage of overall sales

file_loc0 = "https://raw.githubusercontent.com/Barbj379/Two_Ton/main/Item%20Sales%20Report%20(2).csv"
file_loc1 = "https://raw.githubusercontent.com/Barbj379/Two_Ton/main/Profit_Loss.csv"

df_menu = pd.read_csv(file_loc0)
df_pl = pd.read_csv(file_loc1)
#fig = px.bar(bar_data, x="Major Category", y="Net Sales", color="Item Name",
#             barmode="group")

items = df_menu['Major Category'].unique()

app.layout = html.Div(children=[
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Two Ton Dash'),
        html.Div(children='''
            Sales of last fiscal quarter.
        '''),

        dcc.Dropdown(
            id='category-dropdown', clearable=False,
            value=items, options=[
                {'label': c, 'value': c}
                for c in df_menu['Major Category'].unique()
            ]),
        dcc.Graph(id='graph0'),
     #   html.Label([
     #       "Category",
        ]),
    ])


# Callback function that automatically updates the tip-graph based on chosen colorscale
@app.callback(
    Output('graph0', 'figure'),
    [Input("category-dropdown", "value")]
)
def update_figure(Category):
    new_df = df_menu[df_menu['Major Category'] == Category]
    new_df = new_df.groupby(['Minor Category', 'Item Name'])['Net Sales'].sum().reset_index()
    new_df.reset_index()
    fig = px.treemap(new_df, path=['Minor Category', 'Net Sales', 'Item Name'],
                         values='Net Sales', color='Net Sales', color_continuous_scale='RdYlBu',
                         title= 'Net Sales by Craft Beer Product in USD',
                          hover_data=['Item Name'])
    fig.update_traces(root_color="lightgrey")
    fig.update_traces(marker=dict(cornerradius=5))
    return fig


if __name__ == '__main__':
    app.run_server(host='localhost', port=8005)
# Create an app layout