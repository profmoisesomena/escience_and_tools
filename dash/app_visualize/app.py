import dash 
import dash_bootstrap_components as dbc 

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

server = app.server
app.config.suppress_callback_exceptions = True

#reference: https://dash.plotly.com/
#https://dash.plotly.com/dash-core-components/tabs 
#@msocode based in Eric Kleppen code 
#https://medium.com/swlh/dashboards-in-python-for-beginners-and-everyone-else-using-dash-f0a045a86644
#https://medium.com/swlh/dashboards-in-python-3-advanced-examples-for-dash-beginners-and-everyone-else-b1daf4e2ec0a