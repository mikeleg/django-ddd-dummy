from dataclasses import dataclass
from typing_extensions import Self
from typing import Optional


@dataclass(init=True)
class Customer:
    id: Optional[int] = None
    name = str
    surname = str
    phone = str
    email = str

    @staticmethod
    def convert_to_entity(dto: dict) -> "Customer":
        tmp = Customer()
        tmp.id = dto.get("id")
        tmp.name = dto.get("name")
        tmp.surname = dto.get("surname")
        tmp.phone = dto.get("phone")
        tmp.email = dto.get("email")
        return tmp


@dataclass
class Note:
    id: Optional[int] = None
    customer_id = int
    note = str

    @staticmethod
    def convert_into_domain(self, dto: dict) -> Self:
        self.id = dto.get("id")
        self.customer_id = dto.get("customer_id")
        self.note = dto.get("note")

        return self
