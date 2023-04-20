from dataclasses import dataclass

@dataclass(frozen=True)
class Gender:
    MALE = 'male'
    FEMALE = 'female'
