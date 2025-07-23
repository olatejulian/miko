from dataclasses import dataclass

from .direction import DirectionEnum


@dataclass
class MovementIntent:
    direction: DirectionEnum
