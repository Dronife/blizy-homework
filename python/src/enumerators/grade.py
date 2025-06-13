import enum
from typing import Optional

class GradeEnum(enum.Enum):
    APlus = "A+"
    A = "A"
    AB = "AB"
    B = "B"
    C = "C"
    D = "D"
    NONE = "NONE"

    @classmethod
    def get_from_string(cls, grade_string: str) -> Optional['GradeEnum']:
        cleaned = grade_string.strip().upper()
        for member in cls:
            if member.value == cleaned:
                return member
        return None