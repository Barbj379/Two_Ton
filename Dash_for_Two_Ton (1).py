{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from jupyter_dash import JupyterDash"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [],
   "source": [
    "import dash\n",
    "from dash import Dash, dcc, html\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "from jupyter_dash import JupyterDash\n",
    "from dash.dependencies import Input, Output, State"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Running in Jupyter, call the following function to detect the proxy configuration."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_loc = \"https://raw.githubusercontent.com/Barbj379/Two_Ton/main/Item%20Sales%20Report%2011_01_2022-02_16_2023.csv\"\n",
    "\n",
    "df = pd.read_csv(file_loc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Item Name</th>\n",
       "      <th>Global Category</th>\n",
       "      <th>Major Category</th>\n",
       "      <th>Minor Category</th>\n",
       "      <th>Item Quantity</th>\n",
       "      <th>Item/Cover %</th>\n",
       "      <th>Average Item Price</th>\n",
       "      <th>Gross Sales</th>\n",
       "      <th>Net Sales</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4-beer flight</td>\n",
       "      <td>NaN</td>\n",
       "      <td>ALCOHOL</td>\n",
       "      <td>BEER FLIGHTS</td>\n",
       "      <td>648</td>\n",
       "      <td>37.37</td>\n",
       "      <td>9.00</td>\n",
       "      <td>5832</td>\n",
       "      <td>5772.94</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>robot insurance 16oz</td>\n",
       "      <td>NaN</td>\n",
       "      <td>ALCOHOL</td>\n",
       "      <td>16OZ DRAUGHT</td>\n",
       "      <td>575</td>\n",
       "      <td>33.16</td>\n",
       "      <td>8.00</td>\n",
       "      <td>4600</td>\n",
       "      <td>4580.31</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>blood orange blond 16oz</td>\n",
       "      <td>NaN</td>\n",
       "      <td>ALCOHOL</td>\n",
       "      <td>16OZ DRAUGHT</td>\n",
       "      <td>495</td>\n",
       "      <td>28.55</td>\n",
       "      <td>7.77</td>\n",
       "      <td>3845</td>\n",
       "      <td>3842.46</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>low orbit 16oz</td>\n",
       "      <td>NaN</td>\n",
       "      <td>ALCOHOL</td>\n",
       "      <td>16OZ DRAUGHT</td>\n",
       "      <td>341</td>\n",
       "      <td>19.67</td>\n",
       "      <td>8.00</td>\n",
       "      <td>2728</td>\n",
       "      <td>2705.10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>chocolate vanilla porter 10oz</td>\n",
       "      <td>NaN</td>\n",
       "      <td>ALCOHOL</td>\n",
       "      <td>10OZ DRAUGHT</td>\n",
       "      <td>250</td>\n",
       "      <td>14.42</td>\n",
       "      <td>7.00</td>\n",
       "      <td>1750</td>\n",
       "      <td>1731.88</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                       Item Name  Global Category Major Category  \\\n",
       "0                  4-beer flight              NaN        ALCOHOL   \n",
       "1           robot insurance 16oz              NaN        ALCOHOL   \n",
       "2        blood orange blond 16oz              NaN        ALCOHOL   \n",
       "3                 low orbit 16oz              NaN        ALCOHOL   \n",
       "4  chocolate vanilla porter 10oz              NaN        ALCOHOL   \n",
       "\n",
       "  Minor Category  Item Quantity  Item/Cover %  Average Item Price  \\\n",
       "0   BEER FLIGHTS            648         37.37                9.00   \n",
       "1   16OZ DRAUGHT            575         33.16                8.00   \n",
       "2   16OZ DRAUGHT            495         28.55                7.77   \n",
       "3   16OZ DRAUGHT            341         19.67                8.00   \n",
       "4   10OZ DRAUGHT            250         14.42                7.00   \n",
       "\n",
       "   Gross Sales  Net Sales  \n",
       "0         5832    5772.94  \n",
       "1         4600    4580.31  \n",
       "2         3845    3842.46  \n",
       "3         2728    2705.10  \n",
       "4         1750    1731.88  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_beer = pd.DataFrame(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "category = df_beer.groupby(['Major Category', 'Minor Category'])\n",
    "df_category  = category[['Item Quantity', 'Net Sales']].sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Build Dash application"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dash app running on http://127.0.0.1:8050/\n"
     ]
    }
   ],
   "source": [
    "# Run this app with `python app.py` and\n",
    "#visit http://127.0.0.1:8050/ in your web browser.\n",
    "\n",
    "# Build App\n",
    "app = JupyterDash(__name__)\n",
    "\n",
    "# Clear the layout and do not display exception till callback gets executed\n",
    "app.config.suppress_callback_exceptions = True\n",
    "\n",
    "\"\"\"Compute graph data for creating beer sales report\n",
    "Function that takes sales data as input and creates 3 dataframes based on the grouping condition\n",
    "to be used for plotting the charts and graphs.\n",
    "\n",
    "Argument:\n",
    "    df: Filtered dataframe\n",
    "Returns:\n",
    "    Dataframes to create graph.\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "def compute_data_choice(df_beer):\n",
    "    #Total sales by Item Name\n",
    "    tree_data = df.groupby(['Minor Category', 'Item Name'])['Net Sales'].sum().reset_index()\n",
    "    #Item Quantity count\n",
    "    bar_data = df.groupby(['Minor Category', 'Item Name'])['Item Quantity'].sum().reset_index()\n",
    "    #Percentage of overall sales\n",
    "    scatter_data = df.groupby(['Minor Category', 'Item Name'])['Item/Cover %'].sum().reset_index()\n",
    "    return tree_data, bar_data, scatter_data\n",
    "    \n",
    "app.layout = html.Div(children=[\n",
    "        html.H1(children=\"Performance of Craft Beer Products, Trailing Quarter\",\n",
    "                   style={'textAlign': 'center', 'color':'#503D36', 'font-size': 36}),\n",
    "        html.Div([\n",
    "            html.Div([\n",
    "                html.Div([html.H2('Major Category Type', style={'margin-right': '2em'}),\n",
    "                         ]),\n",
    "                  dcc.Dropdown(id='item-name', options=\n",
    "                          [{'label': i, 'value': i}\n",
    "                           for i in df['Major Category'].unique()],\n",
    "                           value='ALCOHOL',\n",
    "                           style={'width': '80%',\n",
    "                                  'height':'3px', \n",
    "                                  'font-size': 18, \n",
    "                                  'textAlign': 'center'}),\n",
    "            ], style={'display':'flex'}),\n",
    "     ]),\n",
    "        \n",
    "            \n",
    "        html.Div([ ], id='plot1'),\n",
    "            \n",
    "        html.Div([\n",
    "            html.Div([ ], id='plot2'),\n",
    "            html.Div([ ], id='plot3')],\n",
    "            style ={'display': 'flex'})\n",
    "        ])\n",
    "        \n",
    "\n",
    "\n",
    "\n",
    "  #Define callback to update graph\n",
    "@app.callback([\n",
    "    Output(component_id='plot1', component_property='children'),\n",
    "    Output(component_id='plot2', component_property='children'),\n",
    "    Output(component_id='plot3', component_property='children')],\n",
    "    [Input(component_id='item-name', component_property='value') ],\n",
    "     [State(\"plot1\", 'children'), State(\"plot2\", \"children\"),\n",
    "             State(\"plot3\", \"children\")]\n",
    ")\n",
    "    \n",
    "    \n",
    "# Add computation to callback function and return graph\n",
    "def get_graph(chart, category, children1, children2):   \n",
    "    #Select data\n",
    "    file_loc = \"https://raw.githubusercontent.com/Barbj379/Two_Ton/main/Item%20Sales%20Report%2011_01_2022-02_16_2023.csv\"\n",
    "    df = pd.read_csv(file_loc)\n",
    "    \n",
    "    # Compute required information for creating graph from the data\n",
    "    tree_data, bar_data, scatter_data = compute_data_choice(df)\n",
    "    \n",
    "    #Percentage of overall sales\n",
    "    scatter_fig = px.scatter(df, x=\"Item Name\", y=\"Item/Cover %\",\n",
    "                 size=\"Net Sales\")\n",
    "    bar_fig = px.bar(df, x='Item Name'[0:25], y='Net Sales', title='Net Sales by Product')\n",
    "    \n",
    "    tree_fig = px.treemap(tree_data, path=['Minor Category', 'Net Sales', 'Item Name'],\n",
    "                         values='Net Sales', color='Net Sales', color_continuous_scale='RdBu',\n",
    "                         title= 'Net Sales by Craft Beer Product in USD',\n",
    "                          hover_data=['Item Name']\n",
    "                                    )\n",
    "    \n",
    "    return [dcc.Graph(figure=tree_fig),\n",
    "            dcc.Graph(figure=bar_fig),\n",
    "            dcc.Graph(figure=scatter_fig)]\n",
    "    \n",
    "    \n",
    "#Run app and display result inline in the notebook\n",
    "app.run_server(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
