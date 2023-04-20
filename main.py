import pandas as pd
from package import ColumnName, Gender, ButterflyChart, FigureHandler, HistogramFactory
from package import DataFrameFilterColumnList, DataFrameFilterColumnValue, OperationType, AppGenerator
import numpy as np
import sys

def find(string: str, substring: str) -> bool:
    return string.find(substring) != -1

def main():
    filename = 'data/vehdrindcr010623.csv'

    df = pd.read_csv(filename, low_memory=False)
    column_names = df.columns.tolist()
    # print('Unfiltered columns:', len(column_names))
    column_names = [c for c in column_names if not (find(c, 'ID') or find(c, 'Id'))]
    # print('Filtered columns based on Id and ID:', len(column_names))
    column_names_str_formatted = '* ' + ('\n* '.join(map(str, column_names)))
    # print(column_names_str_formatted)

    # Filtering logic
    relevant_column_names = [
        ColumnName.age,
        ColumnName.gender,
        ColumnName.speed,
        ColumnName.number_of_fatalities,
        ColumnName.vehicle_year,
        ColumnName.vehicle_make,
        ColumnName.vehicle_model,
        ColumnName.vehicle_towed,
        ColumnName.vehicle_disabled,
        ColumnName.vehicle_plate_state,
        ColumnName.vehicle_oversize,
        ColumnName.vehicle_cargo_spill,
        ColumnName.vehicle_override,
        ColumnName.vehicle_underride,
        ColumnName.vehicle_speed_before_crash,
        ColumnName.vehicle_speed_limit,
        ColumnName.vehicle_maximum_safe_speed,
        ColumnName.initial_impact,
        ColumnName.direction_of_travel,
        ColumnName.first_event,
        ColumnName.second_event,
        ColumnName.third_event,
        ColumnName.fourth_event,
    ]
    df = DataFrameFilterColumnList.filter(df, relevant_column_names)

    # Create app
    ag = AppGenerator(df)
    app = ag.create_app()
    app.run_server(debug=True)

if __name__ == '__main__':
    main()