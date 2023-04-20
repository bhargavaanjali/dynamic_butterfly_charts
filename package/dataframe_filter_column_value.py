import pandas as pd
from typing import List, Any, Tuple
from package.operation_type import OperationType

class DataFrameFilterColumnValue:
    operation_type_to_function = {
        OperationType.EQUAL: lambda df, column_name, value: df[df[column_name] == value],
        OperationType.NOT_EQUAL: lambda df, column_name, value: df[df[column_name] != value],
        OperationType.GREATER_THAN: lambda df, column_name, value: df[df[column_name] > value],
        OperationType.LESS_THAN: lambda df, column_name, value: df[df[column_name] < value],
        OperationType.GREATER_THAN_OR_EQUAL: lambda df, column_name, value: df[df[column_name] >= value],
        OperationType.LESS_THAN_OR_EQUAL: lambda df, column_name, value: df[df[column_name] <= value],
    }

    @staticmethod
    def filter(df: pd.DataFrame, column_name: str, operation_type: OperationType, value: Any) -> pd.DataFrame:
        return DataFrameFilterColumnValue.operation_type_to_function[operation_type](df, column_name, value)

    @staticmethod
    def multifilter(df: pd.DataFrame, filter_parameter_list: List[Tuple[str, OperationType, Any]]) -> pd.DataFrame:
        result = df
        for idx, f in enumerate(filter_parameter_list):
            if f == None:
                continue
            col_name, operation, value = f
            result = DataFrameFilterColumnValue.filter(result, col_name, operation, value)
        return result
