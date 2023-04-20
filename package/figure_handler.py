from typing import Any, List
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go


class FigureHandler:
    def __init__(self,
                figures: List[go.Figure],
                figure_names: List[str],):
        self.__figures = figures
        self.__figure_names = figure_names
        
    def create_app(self) -> dash.Dash:
        attribute_options = [
            ['age', ['==', '>', '<'], [i for i in range(0, 200)]],
            ['gender', ['=='], ['Male', 'Female']],
            ['number_of_fatalities', ['>', '==', '<'], [i for i in range(0, 10000, 1000)]],
            ['speed', ['>', '==', '<'], [i for i in range(0, 500, 10)]]
        ]
        attribute_names = [v[0] for v in attribute_options]
        attribute_operations = ['==', '>', '<', '>=', '<=']
        attribute_values = [i for i in range(0, 200)]
        # app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])
        app = dash.Dash()
        app.layout = html.Div([
            html.Div([
                html.Div(className='attribute1', children=[
                    dcc.Dropdown(
                        id='attribute_name_1',
                        options=[{'label': c, 'value': c} for c in attribute_names],
                        value=None,
                        style=dict(flex=3)
                    ),
                    dcc.Dropdown(
                        id='operation_type_1',
                        options=[{'label': o, 'value': o} for o in attribute_operations],
                        value=None,
                        style=dict(flex=1)
                    ),
                    dcc.Dropdown(
                        id='attribute_value_1',
                        options=[{'label': v, 'value': v} for v in attribute_values],
                        value=None,
                        style=dict(flex=2)
                    ),
                    html.Button(
                        'Clear',
                        id='attribute_1_clear',
                        n_clicks=0,
                        style=dict(flex=0.5)
                    )
                ], style=dict(display='flex')),
                html.Div(className='attribute2', children=[
                    dcc.Dropdown(
                        id='attribute_name_2',
                        options=[{'label': c, 'value': c} for c in attribute_names],
                        value=None,
                        style=dict(flex=3)
                    ),
                    dcc.Dropdown(
                        id='operation_type_2',
                        options=[{'label': o, 'value': o} for o in attribute_operations],
                        value=None,
                        style=dict(flex=1)
                    ),
                    dcc.Dropdown(
                        id='attribute_value_2',
                        options=[{'label': v, 'value': v} for v in attribute_values],
                        value=None,
                        style=dict(flex=2)
                    ),
                    html.Button(
                        'Clear',
                        id='attribute_2_clear',
                        n_clicks=0,
                        style=dict(flex=0.5)
                    )
                ], style=dict(display='flex')),
                html.Div([
                    dcc.Graph(
                        id='chart_primary',
                        style=dict(flex=1),
                        config=dict(responsive=True)
                    ),
                    dcc.Graph(
                        id='chart_secondary',
                        style=dict(flex=1),
                        config=dict(responsive=True)
                    ),
                ], style=dict(display='flex')),
            ])
        ])
    
        @app.callback(
        [
            Output('chart_primary', 'figure'),
            Output('chart_secondary', 'figure')
        ],
        [
            Input('attribute_name_1', 'value'),
            Input('operation_type_1', 'value'),
            Input('attribute_value_1', 'value'),
        ])
        def update_graph(att_name: str, operation: str, value: Any):
            return [self.__figures[0], self.__figures[-1]]

        return app
