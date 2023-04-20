from typing import List

class ButterflyChartNoInputDataError(Exception):
    '''Raised when the input data passed to the butterfly chart is empty'''
    pass

class ButterflyChartInputDataSequencesUnalignedError(Exception):
    '''Raised when the input data sequences passed to the butterfly chart have different lengths'''
    def __init__(self, input_length_1: int, input_length_2: int):
        self.message = f'Input sequence lengths do not match. Got {input_length_1} and {input_length_2}'
        super().__init__(self.message)

class ButterflyChartLabelsMisalignedWithDataError(Exception):
    '''Raised when the input data sequences passed to the butterfly chart have different lengths to the y labels'''
    def __init__(self, input_length: int, y_labels_length: int):
        self.message = f'Input sequence length does not match with y labels. Got input length as {input_length} and y label length as {y_labels_length}'
        super().__init__(self.message)

class ButterflyChartInputDataFrameKeyError(Exception):
    '''Raised when we try to plot something which does not exist in the dataframe'''
    def __init__(self, keyerror: str, column_names: List[str]):
        column_names_string = f"\n* ".join(column_names)
        self.message = f'Could not find {keyerror} in the input dataframe with the following columns:\n* {column_names_string}'
        super().__init__(self.message)

