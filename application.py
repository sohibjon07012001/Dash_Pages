import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html


application = dash.Dash(use_pages=True, suppress_callback_exceptions=True,
                        external_stylesheets=[
                            dbc.themes.MATERIA, dbc.icons.FONT_AWESOME])


application.layout = html.Div([
    dbc.Row([
        dbc.Col(md=3),
        dbc.Col(dbc.Button("Error Page",href="dashboard/test"),),
        dbc.Col(dbc.Button("Main Page",href="/" ),),
    ]),
    dash.page_container
])



if __name__ == "__main__":
    application.run_server(debug=True)
