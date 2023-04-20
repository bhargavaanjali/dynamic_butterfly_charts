from package.bin_formatter import BinFormatter

from typing import List

class BinFormatterAdult(BinFormatter):
    def format(self, bins: List[int]) -> List[str]:
        age_bins = []
        string_width = 3
        total_string_length = 2*string_width + 1  # For the two ages and the hyphen
        for i in range(len(bins)-1):
            begin = str(bins[i]).rjust(string_width, ' ')
            end = str(bins[i+1]-1).ljust(string_width, ' ')
            if i != len(bins)-2:
                bin_str = f'{begin}-{end}'
                age_bins.append(bin_str)
                total_string_length = len(bin_str)
            else:
                final_string = f'> {begin}'  # '> 80'
                prev_l = len(final_string)
                justified_len = (total_string_length*2)//3
                # [' '] * 
                age_bins.append(final_string)
        return age_bins
