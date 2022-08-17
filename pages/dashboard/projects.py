import dash_bootstrap_components as dbc
import dash 
from dash import html, dcc, dash_table, callback, Input, Output, State, ctx
from dash.exceptions import PreventUpdate
import dash_mantine_components as dmc
dash.register_page(__name__)




layout = html.Div(children=[
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Loading(dash_table.DataTable(
                        id='tbl_projects',
                        data=[],
                        columns=[{'id': 'Title', 'name':'Title'},{'id':'Created', 'name':'Created'}, 
                        {'id':'User', 'name':'User'}, {'id':'Dataset Attached', 'name':'Dataset Attached'}, {'id':'Delete Project', 'name':'Delete Project'}, 
                        {'id':'Update Project', 'name':'Update Project'}],
                        style_cell={'textAlign': 'center',
                                    'padding': '5px'},
                         style_data_conditional=[
                            {
                                'if': {
                                    'state': 'active'  # 'active' | 'selected'
                                },
                            'backgroundColor': 'rgba(0, 116, 217, 0.5)',
                            'border': 'none'#'1px solid rgb(0, 116, 217)'
                            },
                            {
                                'if': {
                                    'state': 'active',
                                    'column_id': 'Delete Project',
                                    
                                },
                                'color': 'tomato',
                                'font-size': '20px',
                                'wontWeigth':'bold'
                            },
                            {
                                'if': {
                                    'column_id': 'Update Project',
                                    'state': 'active',
                                },
                                'color': 'green',
                                'fontWeight': 'bold'
                            },
                         ],
                        sort_mode="multi",
                        page_action="native",
                        style_header={
                            'backgroundColor': '#e4ebf5',
                            'fontWeight': 'bold',
                            # 'border': '1px solid black',
                            'font-size': '13px',
                            'border':'none'
                        },
                        style_data={'backgroundColor':'#e4ebf5', 'border':'none'},
                        style_table={'overflowY': 'auto', 'height': 220},
                        page_size=5,
                        filter_action="native",
                        sort_action="native",
                        page_current= 0,
                        style_as_list_view=True,
                        ),type="dot", className='dbc'),
                    ])
                ],style={'border-radius':'5px', "width": "20rem",'height': 290},  color="#e4ebf5", outline=False, body=False)
            ]),
            ],md=8),
            dcc.Location(id="url", refresh=True),
            dcc.Location(id="url1", refresh=True),
            dcc.Interval(
            id='interval_component_projects',
            interval=10 * 60 * 1000,
            n_intervals=0),
            dbc.Col([
                dbc.CardGroup([
                dbc.Card([
                    dbc.CardBody([
                        html.Div([
                            html.Div(html.Center(html.I(className="fas fa-file-circle-plus fa-5x")),style={'margin-top':'25px'}),
                            html.Center(html.H4('Create a new project'), style={'margin-top':'25px'}),
                            dmc.Space(h="md"),
                            html.Center(dmc.Button("Create",variant="gradient", size='lg', gradient={"from": "teal", "to": "blue", "deg": 60},id="project_button", n_clicks=0, class_name='mb-3 mt-2'))

                        ],style={'flex-direction':'column'})
                    ])
                ],style={'border-radius':'15px', "width": "10rem"},  color="#e4ebf5", outline=False, body=False)
            ]),
            html.Div(
                id='hidden_div_for_redirect_callback'
            ),
            html.Div(
                    [
                        dbc.Modal(
                            [
                                dbc.ModalHeader(dbc.ModalTitle("Are you sure you want to remove this project?"), close_button=True),
                               
                                dbc.ModalFooter(
                                    dcc.Link(dbc.Button(
                                        "Yes",
                                        id="close_centered",
                                        className="ms-auto",
                                        n_clicks=0,
                                    ),href="/dashboard/projects", refresh=True)
                                ),
                            ],
                            id="modal-centered",
                            centered=True,
                            is_open=False,
                        ),
                    ]
                ),
               
                html.Div(id='test'),
                html.Div(id='test1')
            ])
        ])
])

