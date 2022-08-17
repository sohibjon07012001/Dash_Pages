import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html


application = dash.Dash(use_pages=True, suppress_callback_exceptions=True,
                        external_stylesheets=[
                            dbc.themes.MATERIA, dbc.icons.FONT_AWESOME])


sidebar = html.Div(
    [
        html.Div(
            [
                html.H2("Auto ML", style={'color': 'white'}),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"),
                     html.Span("Dashboard")],
                    href=dash.page_registry['pages.dashboard']['path'],
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-calendar-alt me-2"),
                        html.Span("Projects"),
                    ],
                    href=dash.page_registry['pages.dashboard.projects']['path'],
                    active="exact",
                    
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-envelope-open-text me-2"),
                        html.Span("Datasets"),
                    ],
                    href=dash.page_registry['pages.dashboard.datasets']['path'],
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar"
)






application.layout = html.Div([dcc.Location(id="url"),
                                        sidebar,
                                        html.Div(children=[
                                            dbc.Row(
                                                dbc.Breadcrumb(id='breadcrumb')
                                            ),

                                             dash.page_container
                                        ], id="page-content", className="content"),
                                        dcc.Store(id='store_projects', storage_type='session'),
])



if __name__ == "__main__":
    application.run_server(debug=False)
