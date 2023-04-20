import pandas as pd
from typing import List

class DataFrameFilterColumnList:
    @staticmethod
    def filter(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
        return df[columns]
