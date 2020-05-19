import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import sqlite3
import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import numpy as np




data =pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv',sep=',')
#redefine columns
data.columns=['data','pais','estado','lat','long','conf','recov','death']
#define and get top countries
top_list_countries = data.groupby(by='pais').max().sort_values('conf', ascending=False).head(6).index
#filter by top countries
data_country = data.loc[data['pais'].isin(top_list_countries)]
#get data where state is null and put result in df_res
df = data_country.loc[data_country['estado'].isin([np.nan,''])]
