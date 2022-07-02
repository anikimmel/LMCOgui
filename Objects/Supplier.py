from dataclasses import dataclass
from typing import List


@dataclass
class Business:
    name: str
    methods: List[str]

    def hasMethod(self, method):
        return method in self.methods
