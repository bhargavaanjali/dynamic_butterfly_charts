
from abc import ABC, abstractclassmethod
from typing import List

class BinFormatter(ABC):
    @abstractclassmethod
    def format(self, bins: List[int]) -> List[str]:
        raise NotImplementedError()
