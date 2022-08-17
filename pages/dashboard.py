import dash_bootstrap_components as dbc
import dash
from dash import html, dcc
import plotly.graph_objects as go
dash.register_page(__name__)



labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

# pull is given as a fraction of the pie radius
fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0, 0.2, 0])])
fig.update_xaxes(showgrid=False, )
fig.update_yaxes(showgrid=False, categoryorder='total ascending',
                     ticksuffix=' ', showline=False)
fig.update_traces(hovertemplate=None, marker=dict(line=dict(width=0)))
fig.update_layout(title="Projects",
                      margin=dict(t=80, b=0, l=70, r=40),
                      hovermode="x unified",
                      xaxis_title=' ', yaxis_title=" ",
                      xaxis={'type': 'category'},
                      title_font=dict(size=25, color='#8a8d93',
                                      family="Lato, sans-serif"),
                      font=dict(color='#8a8d93'),
                      paper_bgcolor='#e4ebf5',
                      plot_bgcolor='#e4ebf5',
                      legend=dict(orientation="h", yanchor="bottom",
                                  y=1, xanchor="center", x=0.5),
                      hoverlabel=dict(bgcolor="black", font_size=13, font_family="Lato, sans-serif"))

layout = html.Div(children=[
    dbc.Row([
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(figure=fig)
                    ])
                ],style={'border-radius':'15px', "width": "10rem"},  color="#e4ebf5", outline=False, body=False)
            ])
        ],md=4),

        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    dbc.CardBody([
                        html.P('Infastructure Statistics')
                    ])
                ],style={'border-radius':'15px', "width": "10rem"},  color="#e4ebf5", outline=False, body=False)
            ])
        ],md=4)

    ])
])



