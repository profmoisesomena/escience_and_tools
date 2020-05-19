import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from app import app
from database import dataset_load
#import plotly.graph_objects as go # or plotly.express as px
import plotly.express as px

df = dataset_load.df

#Define Graph
fig = px.line(df, x="data", y="conf",color='pais')


############################################### CODIGO MODIFICANDO ##################################################################
layout = html.Div(
            id='table-paging-with-graph-container',
            className="five columns"
        )





#define layout of result page
layout = html.Div([
    dcc.Dropdown(
        id='my-dropdown',
        options=[
        {'label': i, 'value': i} for i in df.pais.unique()
        ],
        multi=True,
        placeholder ='Filtrar por país',
        value='Brazil'
    ),
    
    dcc.Graph(id='my-graph',figure=fig)
],style={'width': '500'})



#callback filter
@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_output_1(value):
    # Safely reassign the filter to a new variable
    filtered_df = df.loc[df['pais'].isin(value)]
    fig = px.line(filtered_df, x="data", y="conf",color='pais')
    return fig


