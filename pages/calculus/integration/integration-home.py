import dash
from dash import html

dash.register_page(__name__, path='/calculus/integration')

layout = html.Div([
    html.H1('You reached the integration page')
])