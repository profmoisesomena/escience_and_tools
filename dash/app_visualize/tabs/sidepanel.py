import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas
from dash.dependencies import Input, Output

from app import app

from tabs import tab_describe, tab_data, tab_line,tab_marker
from database import dataset_load

layout = html.Div([
    html.H1('Analyse Data App')
    ,dbc.Row([dbc.Col(
        html.Div([
         html.H3('Summary Fast analyse')
        ,html.Div(
            [
            html.H5('Version Alfa 0.1')
            ]
        )
    
        ])
    , width=3)
    ,dbc.Col(html.Div([
            dcc.Tabs(id="tabs", value='tab-1', children=[
                    dcc.Tab(label='Data Table', value='tab-1'),
                    dcc.Tab(label='Describe Info', value='tab-2'),
                    dcc.Tab(label='Line Graph', value='tab-3'),
                    dcc.Tab(label='Marker Graph',value='tab-4'),                ])
            , html.Div(id='tabs-content')
        ]))
    
    ])
])