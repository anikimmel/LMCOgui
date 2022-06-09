from dataclasses import dataclass
from typing import List


@dataclass()
class Process:
    name: str
    part: str
    material: str
    weight: float
    cost: float
    time: float
    score: int
    task_sequence: List[str]



