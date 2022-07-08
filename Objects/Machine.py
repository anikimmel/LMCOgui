from dataclasses import dataclass


@dataclass
class Machine:
    MachineName: str
    Type: str
    ShiftSchedule: str
    MaintenanceCycle: int
    LastMainentance: str
    TimeCoefficient: float
    CostCoefficient: float
