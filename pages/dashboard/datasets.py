import dash_bootstrap_components as dbc
import dash 
from dash import html, dcc

dash.register_page(__name__)

layout = html.Div([
    html.Center([
        html.H1('Datasets Page')
    ]),
    html.H1(["Datasets"])
])
