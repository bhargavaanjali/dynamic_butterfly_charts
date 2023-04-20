from package.histogram_creator import *
from package.bin_formatter_adult import BinFormatterAdult
from package.bin_formatter_teen import BinFormatterTeen

class HistogramFactory:
    @staticmethod
    def createAdultHistogramCreator() -> HistogramCreator:
        bin_formatter = BinFormatterAdult()
        return HistogramCreator(bin_formatter)
    
    @staticmethod
    def createTeenHistogramCreator() -> HistogramCreator:
        bin_formatter = BinFormatterTeen()
        return HistogramCreator(bin_formatter)
