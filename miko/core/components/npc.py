from dataclasses import dataclass


@dataclass
class NPC:
    dialog_id: str
    wander: bool = False
