from dataclasses import dataclass
from datetime import date


@dataclass
class Dummy:
    id: int
    name: str
    surname: str
    age: int
    address: str
    created_at: date
    updated_at: date
