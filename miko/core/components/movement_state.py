from dataclasses import dataclass
from enum import Enum, auto


class MovementStatus(Enum):
    IDLE = auto()
    MOVING = auto()


@dataclass
class MovementState:
    status: MovementStatus = MovementStatus.IDLE
    moved_pixels: int = 0
