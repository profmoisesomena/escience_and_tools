import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from tabs import tab_data, tab_describe,tab_line, sidepanel, tab_marker
from database import dataset_load
import sqlite3
from dash.dependencies import Input, Output
import pandas as pd


app.layout = sidepanel.layout

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
       return tab_data.layout
    elif tab == 'tab-2':
       return tab_describe.layout
    elif tab == 'tab-3':
        return tab_line.layout
    elif tab == 'tab-4':
        return tab_marker.layout




if __name__ == '__main__':
    app.run_server(debug = True)