import Process
from dataclasses import dataclass
from typing import List


@dataclass
class Design:
    name: str
    image: str  # string to file location of image
    processes: List[Process]
