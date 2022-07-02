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
    methods: List[str]
    task_sequence: List[str]



