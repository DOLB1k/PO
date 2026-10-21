from dataclasses import dataclass
from datetime import date, timedelta


class CirculationError(Exception):
    pass


@dataclass
class Reader:
    id: int
    active: bool = True
    overdue: int = 0


def issue_book(reader: Reader, available: bool, today: date) -> date:
    if not reader.active:
        raise CirculationError("Reader is blocked")
    if reader.overdue > 0:
        raise CirculationError("Unresolved overdue loans")
    if not available:
        raise CirculationError("No available instance")
    return today + timedelta(days=14)