from package.bin_formatter import BinFormatter
from package.column_name import ColumnName
from package.gender import Gender
from typing import List, Dict
import pandas as pd
import numpy as np

class HistogramCreator:
    def __init__(self, bin_formatter: BinFormatter):
        self.bin_formatter = bin_formatter
    
    def create_dataframe_from_bins(
            self,
            bins: List[int],
            input_dict: Dict[Gender, pd.DataFrame]) -> pd.DataFrame:
        '''
        Creates a pandas dataframe using the bins and dataframe to store the histogram
        '''

        overspeeding_fatalities_male, overspeeding_fatalities_female = input_dict[Gender.MALE], input_dict[Gender.FEMALE]
        min_age, max_age = bins[0], bins[-1]-1
        overspeeding_fatalities_male = overspeeding_fatalities_male[overspeeding_fatalities_male[ColumnName.age] >= min_age]
        overspeeding_fatalities_male = overspeeding_fatalities_male[overspeeding_fatalities_male[ColumnName.age] <= max_age]

        overspeeding_fatalities_female = overspeeding_fatalities_female[overspeeding_fatalities_female[ColumnName.age] >= min_age]
        overspeeding_fatalities_female = overspeeding_fatalities_female[overspeeding_fatalities_female[ColumnName.age] <= max_age]


        male_overspeeding_fatalities_hist, _ = np.histogram(
            overspeeding_fatalities_male[ColumnName.age].tolist(),
            bins=bins
        )
        female_overspeeding_fatalities_hist, _ = np.histogram(
            overspeeding_fatalities_female[ColumnName.age].tolist(),
            bins=bins
        )
        age_bins = self.bin_formatter.format(bins)
        data = {
            Gender.MALE: male_overspeeding_fatalities_hist,
            Gender.FEMALE: female_overspeeding_fatalities_hist,
            'age': age_bins,
        }
        return pd.DataFrame(data)