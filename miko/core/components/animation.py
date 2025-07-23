from dataclasses import dataclass


@dataclass
class Animation:
    current_frame: int
    frame_time: float
    elapsed_time: float
    frames: list[int]
