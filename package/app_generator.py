
import pandas as pd
import dash
import base64
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from typing import Dict, List, Any
from package import ColumnName, Gender, Age, OperationType, DataFrameFilterColumnValue, HistogramFactory, ButterflyChart, FigureHandler
from collections import defaultdict

class AppGenerator:
    def __init__(self, dataframe: pd.DataFrame):
        self.__dataframe = dataframe
        self.__filtering_parameters = [None, None]
        self.__figures = None
        self.__figure_names = None
        self.bins = {
            Age.ADULT: [0, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 80, 200],
            Age.TEEN: [i for i in range(15, 21)]
        }
        self.possible_values_from_column_name = self.get_possible_values_from_columns_in_dataframe(self.__dataframe)
    
    def get_possible_values_from_columns_in_dataframe(self, dataframe: pd.DataFrame) -> Dict[str, List[Any]]:
        # Create possible column values
        column_values_map = {None: None}
        for c in dataframe.columns.tolist():
            column_values_map[c] = sorted(dataframe[c].dropna().unique().tolist())
        return column_values_map

    def create_histograms_using_filtering_parameters(self):
        df = DataFrameFilterColumnValue.multifilter(self.__dataframe, self.__filtering_parameters)
        # Separate based on gender
        male_gender_id, female_gender_id = 1, 2
        multifiltered_male_df = DataFrameFilterColumnValue.filter(df, ColumnName.gender, OperationType.EQUAL, male_gender_id)
        multifiltered_female_df = DataFrameFilterColumnValue.filter(df, ColumnName.gender, OperationType.EQUAL, female_gender_id)
        input_data_dict = {
            Gender.MALE: multifiltered_male_df,
            Gender.FEMALE: multifiltered_female_df
        }
        self.filtered_df = df
        # Create histograms based on age on the male and female overspeeders
        teen_df = HistogramFactory.createTeenHistogramCreator().create_dataframe_from_bins(self.bins[Age.TEEN], input_data_dict)
        adult_df = HistogramFactory.createAdultHistogramCreator().create_dataframe_from_bins(self.bins[Age.ADULT], input_data_dict)

        return {Age.TEEN: teen_df, Age.ADULT: adult_df}
    
    def create_chart_title_from_filters(self):
        filter_strs = [' '.join(map(str, f)) for f in self.__filtering_parameters if f != None]
        return ' & '.join(filter_strs)
    
    def create_butterfly_charts(self, histogram_dataframes: Dict[Age, pd.DataFrame]) -> Dict[Age, ButterflyChart]:
        # Now we can create the butterfly chart
        chart_title = self.create_chart_title_from_filters()  #  'Number of overspeeding fatalities'
        counts = {Age.ADULT: {Gender.MALE: 0, Gender.FEMALE: 0}, Age.TEEN: {Gender.MALE: 0, Gender.FEMALE: 0}}
        for i in histogram_dataframes.keys():
            counts[i][Gender.MALE] = sum(histogram_dataframes[i][Gender.MALE])
            counts[i][Gender.FEMALE] = sum(histogram_dataframes[i][Gender.FEMALE])
        bfc_objs = {}
        for i in Age.values():
            bfc_objs[i] = ButterflyChart(histogram_dataframes[i], 'male', 'female', 'age', f'{chart_title} for {i}s (M: {counts[i][Gender.MALE]} F: {counts[i][Gender.FEMALE]})')
        return bfc_objs
    
    def update_figures(self):
        dfs = self.create_histograms_using_filtering_parameters()
        bfc_objs = self.create_butterfly_charts(dfs)
        self.__figure_names, self.__figures = {}, {}  # Clearing the existing stuff
        for i in Age.values():
            self.__figure_names[i] = bfc_objs[i].title_name
            self.__figures[i] = bfc_objs[i].create_figure()
    
    def create_app(self):
        if not self.__figures:
            self.update_figures()

        attribute_names = self.__dataframe.columns.to_list()

        attribute_operations = [
            OperationType.EQUAL,
            OperationType.GREATER_THAN,
            OperationType.LESS_THAN,
            OperationType.GREATER_THAN_OR_EQUAL,
            OperationType.LESS_THAN_OR_EQUAL,
        ]

        attribute_values = [i for i in range(0, 200)]
        attribute_values.append('YES')
        attribute_values.append('NO')

        # app = dash.Dash(external_stylesheets=[dbc.themes.UNITED])
        app = dash.Dash()
        app.layout = html.Div([
            html.Div(
                id='page_title', children=[
                    html.H2(
                        'Dynamic Data Plotter',
                        style={'text-align': 'center'}
                    )
                ]
            ),
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
            ]),
            html.Div([ 
                html.Button("Download CSV", id="btn_csv", style={'margin-left': '47vw', 'padding': '15px', 'background-color': '#ed7d31', 'color': 'white', 'border': 'none', 'border-radius': '10px'}),
                dcc.Download(id="download-dataframe-csv"),  
            ]),
        ])

        @app.callback(
            Output('attribute_value_1', 'options'),
            Input('attribute_name_1', 'value')
        )
        @app.callback(
            Output('attribute_value_2', 'options'),
            Input('attribute_name_2', 'value')
        )
        def dynamic_dropdown_options_update(att_name: str) -> List[Dict[str, Any]]:
            options = self.possible_values_from_column_name[att_name]
            if not options:
                return []
            return [{'label': i, 'value': i} for i in options]

        @app.callback(
            Output("download-dataframe-csv", "data"),
            Input("btn_csv", "n_clicks"),
            prevent_initial_call=True,
        )
        def func(n_clicks):
            return dcc.send_data_frame(self.filtered_df.to_csv, "mydf.csv")

        @app.callback(
        [
            Output('chart_primary', 'figure'),
            Output('chart_secondary', 'figure'),
            Output('attribute_name_1', 'value'),
            Output('operation_type_1', 'value'),
            Output('attribute_value_1', 'value'),
            Output('attribute_name_2', 'value'),
            Output('operation_type_2', 'value'),
            Output('attribute_value_2', 'value'),
        ],
        [
            Input('attribute_name_1', 'value'),
            Input('operation_type_1', 'value'),
            Input('attribute_value_1', 'value'),
            Input('attribute_name_2', 'value'),
            Input('operation_type_2', 'value'),
            Input('attribute_value_2', 'value'),
            Input('attribute_1_clear', 'n_clicks'),
            Input('attribute_2_clear', 'n_clicks'),
        ])
        def update_graph(
                att_name_1: str,
                operation_1: str,
                value_1: Any,
                att_name_2: str,
                operation_2: str,
                value_2: Any,
                att_1_clear_nclicks: int,
                att_2_clear_nclicks: int):
            
            activated_button_name = dash.callback_context.triggered_id
            att_1, att_2 = [att_name_1, operation_1, value_1], [att_name_2, operation_2, value_2]
            is_att_1_invalid, is_att_2_invalid = any([i==None for i in att_1]), any([i==None for i in att_2])

            clear_button_ids = ['attribute_1_clear', 'attribute_2_clear']
            is_att_clear = [activated_button_name == clear_button_ids[i] for i in range(len(clear_button_ids))]

            if is_att_1_invalid and is_att_2_invalid:
                reversed_age_categories = Age.values()
                reversed_age_categories.reverse()
                return [self.__figures[i] for i in reversed_age_categories] + (att_1, [None, None, None])[is_att_clear[0]] + (att_2, [None, None, None])[is_att_clear[1]]
            
            for idx, (invalidity, filter) in enumerate(zip([is_att_1_invalid, is_att_2_invalid], [att_1, att_2])):
                # All the values of the attributes should be set at this point and we can use it for filtering
                if not invalidity:
                    self.__filtering_parameters[idx] = filter
            
            for idx, is_cleared in enumerate(is_att_clear):
                if is_cleared:
                    self.__filtering_parameters[idx] = None
            
            self.update_figures()
            reversed_age_categories = Age.values()
            reversed_age_categories.reverse()

            # Set the attribute values
            attributes = []
            for i, (a, is_clear) in enumerate(zip([att_1, att_2], is_att_clear)):
                attributes = attributes + (a, [None, None, None])[is_clear]
            return [self.__figures[i] for i in reversed_age_categories] + attributes

        return app

    