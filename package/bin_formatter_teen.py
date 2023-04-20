from package.bin_formatter import BinFormatter

from typing import List

class BinFormatterTeen(BinFormatter):
    def format(self, bins: List[int]) -> List[str]:
        age_bins = []
        for i in range(len(bins)-1):
            begin = str(bins[i]).ljust(5, ' ')
            # begin = begin.rjust(4, ' ')
            age_bins.append(begin)
        return age_bins