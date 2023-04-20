from typing import List, Any
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from package.butterfly_chart_errors import *

class ButterflyChart:
    '''This class is a wrapper around plotly to add a butterfly chart in a simple manner'''
    def __init__(
            self,
            df: pd.DataFrame,
            x_axis_left_name: str,
            x_axis_right_name: str,
            y_axis_name: str,
            title_name: str):
        try:
            self.x_left = df[x_axis_left_name].tolist()
            self.x_right = df[x_axis_right_name].tolist()
            self.y_axis = df[y_axis_name].tolist()
            self.x_axis_left_name = x_axis_left_name
            self.x_axis_right_name = x_axis_right_name
            self.y_axis_name = y_axis_name
            self.title_name = title_name

            l1, l2, yl = len(self.x_left), len(self.x_right), len(self.y_axis)
            if (l1 != l2):
                raise ButterflyChartInputDataSequencesUnalignedError(l1, l2)
            if l1 == 0:
                raise ButterflyChartNoInputDataError
            if l1 != yl:
                raise ButterflyChartLabelsMisalignedWithDataError(l1, yl)
            
            self.max_x_value = max(max(self.x_left), max(self.x_right))
        except KeyError as e:
            raise ButterflyChartInputDataFrameKeyError(str(e), df.columns.tolist())
    
    def create_figure(
            self,
            left_marker_color: str = '#4472c4',
            right_marker_color: str = '#ed7d31') -> go.Figure:
        # Create butterfly chart based on gender, age and histogram created above
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{}, {}]],
            shared_xaxes=False,
            shared_yaxes=False,
            horizontal_spacing=0.08 
        )

        fig.append_trace(go.Bar(
            x=self.x_left,
            y=self.y_axis,
            hovertemplate=self.x_axis_left_name + ' %{y}<br><b>Value</b>: %{x}<br>',
            # text=text_list.map('{:,.0f}'.format), #Display the numbers with thousands separators in hover-over tooltip 
            textposition='inside',
            orientation='h', 
            width=0.7, 
            showlegend=False, 
            marker_color=left_marker_color), 
            1, 1
        ) # 1, 1 represents row 1 column 1 in the plot grid

        fig.append_trace(go.Bar(
            x=self.x_right,
            y=self.y_axis,
            hovertemplate=self.x_axis_right_name + ' %{y}<br><b>Value</b>: %{x}<br>',textposition='inside',
            orientation='h', 
            width=0.7, 
            showlegend=False, 
            marker_color=right_marker_color), 
            1, 2
        ) # 1, 2 represents row 1 column 2 in the plot grid

        fig.update_xaxes(
            showticklabels=True,
            title_text=self.x_axis_left_name,
            row=1,
            col=1,
            range=[self.max_x_value, 0]
        )

        fig.update_xaxes(
            showticklabels=True,
            title_text=self.x_axis_right_name,
            row=1,
            col=2,
            range=[0, self.max_x_value]
        )
        fig.update_yaxes(
            row=1,
            col=1,
            showticklabels=False
        )   
        fig.update_layout(
            title={
                'text': self.title_name,
                'y':0.9,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'
            },
            xaxis1={'side': 'bottom'},
            xaxis2={'side': 'bottom'},
        )

        return fig

        
