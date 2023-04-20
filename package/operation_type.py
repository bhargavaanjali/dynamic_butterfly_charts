from dataclasses import dataclass

@dataclass(frozen=True)
class OperationType:
    EQUAL: str = '=='
    NOT_EQUAL: str = '!='
    GREATER_THAN: str = '>'
    LESS_THAN: str = '<'
    GREATER_THAN_OR_EQUAL: str = '>='
    LESS_THAN_OR_EQUAL: str = '<='