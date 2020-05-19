import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

#reference : https://dash.plotly.com/layout

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


from database import dataset_load
df = dataset_load.df
#data.columns=['data','pais','estado','lat','long','conf','recov','death']

layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df[df['pais'] == i]['conf'],
                    y=df[df['pais'] == i]['death'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.pais.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'Casos'},
                yaxis={'title': 'Mortes'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])
