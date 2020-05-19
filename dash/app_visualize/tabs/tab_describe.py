import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html 
import dash_bootstrap_components as dbc 
import dash_table
import pandas as pd
from dash.dependencies import Input, Output

from app import app 
from database import dataset_load

df_normalizado = dataset_load.df

stat_number_norm = df_normalizado.describe(include='all').T.reset_index()
#stat_number_norm['skewness'] =pd.Series(df_normalizado.skew())
#stat_number_norm['median'] =pd.Series(df_normalizado.median())
#stat_number_norm['kurtosis'] =pd.Series(df_normalizado.kurtosis())
#stat_number_norm['type'] =pd.Series(df_normalizado.dtypes)
#stat_number_norm['nulos'] =pd.Series(df_normalizado.isna().sum())
#stat_number_norm = stat_number_norm[['type','count', 'mean', 'std', 'min', 'max', 'nulos', 'median','skewness','kurtosis']]
stat_number_norm = stat_number_norm.fillna('-')


PAGE_SIZE = 50
#  html.Div([
#         dbc.Row([dbc.Col(html.Div(html.P("A single, half-width column")),style = {'padding':'50px'})
#                 ,dbc.Col(
layout =html.Div(dash_table.DataTable(
                            id='table-sorting-filtering_d',
                            columns=[
                                {'name': i, 'id': i, 'deletable': True} for i in stat_number_norm
                            ],
                            style_table={'height':'750px','width':'1024'
                                ,'overflowX': 'scroll'},

                            style_data_conditional=[
                                {
                                    'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'
                                }
                            ],
                            style_cell={
                                'height': '90',
                                # all three widths are needed
                                'minWidth': '140px', 'width': '140px', 'maxWidth': '140px', 'textAlign': 'center'
                                ,'whiteSpace': 'normal'
                            }
                            ,style_cell_conditional=[
                                {'if': {'column_id': 'description'},
                                'width': '48%'},
                                {'if': {'column_id': 'title'},
                                'width': '18%'},
                            ]
                            , page_current= 0,
                            page_size= PAGE_SIZE,
                            page_action='custom',

                            filter_action='custom',
                            filter_query='',

                            sort_action='custom',
                            sort_mode='multi',
                            sort_by=[]
                        )
                        )
            #             , width=9)
            #     ])
            # ])

operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]


def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3


@app.callback(
    Output('table-sorting-filtering_d', 'data')
    , [Input('table-sorting-filtering_d', "page_current")
     , Input('table-sorting-filtering_d', "page_size")
     , Input('table-sorting-filtering_d', 'sort_by')
     , Input('table-sorting-filtering_d', 'filter_query')

     ])
def update_table_2(page_current, page_size, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = stat_number_norm

    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff = dff.loc[dff[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    page = page_current
    size = page_size
    return dff.iloc[page * size: (page + 1) * size].to_dict('records')