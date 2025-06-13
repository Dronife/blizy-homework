import enum
from typing import Optional

class ConditionEnum(enum.Enum):
    USED = "USED"

    @classmethod
    def get_from_string(cls, condition: str) -> Optional['ConditionEnum']:
        cleaned = condition.strip().upper()
        for member in cls:
            if member.value == cleaned:
                return member
        return None