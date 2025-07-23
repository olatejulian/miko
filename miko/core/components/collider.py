from dataclasses import dataclass


@dataclass
class Collider:
    width: int
    height: int
    is_solid: bool = True
