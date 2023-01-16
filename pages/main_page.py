import dash_bootstrap_components as dbc
import dash
from dash import html, dcc
import plotly.graph_objects as go
dash.register_page(__name__)


dash.register_page(__name__,
                   path_template="/")


def layout():
    return html.Div([
        html.Center(html.H1("Main Page"))
    ])