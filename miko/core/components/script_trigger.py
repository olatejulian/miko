from dataclasses import dataclass


@dataclass
class ScriptTrigger:
    trigger_type: str
    script_id: str
