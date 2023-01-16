import dash_bootstrap_components as dbc
import dash
from dash import html, dcc
import plotly.graph_objects as go
dash.register_page(__name__)


dash.register_page(__name__,
                   path_template="dashboard/<project_name>")


def layout(project_name=None):
    return html.Div([
        project_name,
        html.Iframe(
            src="assets/census_report.html",  # must be under assets/ to be properly served
            style={"height": "1080px", "width": "100%"},
        )
    ])