import dash
from dash import html

dash.register_page(__name__, path='/calculus/derivatives', name="Derivatives", order=3)

layout = html.Div([
    html.H1('You reached the derivatives page')
])