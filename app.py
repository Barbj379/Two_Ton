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

df = pd.read_csv('https://raw.githubusercontent.com/Barbj379/Two_Ton/main/Item%20Sales%20Report.csv')

#fig = px.bar(bar_data, x="Major Category", y="Net Sales", color="Item Name",
#             barmode="group")

items = df['Major Category'].unique()

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
                for c in df['Major Category'].unique()
            ]),
        dcc.Graph(id='graph0'),
        html.Label([
            "Category",
        ]),
    ])
])


# Callback function that automatically updates the tip-graph based on chosen colorscale
@app.callback(
    Output('graph0', 'figure'),
    [Input("category-dropdown", "value")]
)
def update_figure(Category):
    new_df = df[df['Major Category'] == Category]
    new_df = new_df.groupby(['Minor Category', 'Item Name'])['Net Sales'].sum().reset_index()
    new_df.reset_index()
    fig = px.bar(
        new_df, x="Minor Category", y="Net Sales", color="Item Name",
        color_continuous_scale=Category,
        title="Items")
    return fig


if __name__ == '__main__':
    app.run_server(host='localhost', port=8005)
# Create an app layout