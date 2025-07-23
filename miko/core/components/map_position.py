from dataclasses import dataclass


@dataclass
class MapPosition:
    map_name: str
    tile_x: int
    tile_y: int
