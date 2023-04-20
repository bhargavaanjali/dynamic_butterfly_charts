from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Age:
    TEEN: str = 'teen'
    ADULT: str = 'adult'

    @staticmethod
    def values():
        return [Age.TEEN, Age.ADULT]
