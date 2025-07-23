from dataclasses import dataclass
from enum import Enum, auto


class DirectionEnum(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()


@dataclass
class Direction:
    value: DirectionEnum
