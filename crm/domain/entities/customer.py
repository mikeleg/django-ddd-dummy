from dataclasses import dataclass


@dataclass
class Customer:
    id = int
    name = str
    surname = str
    phone = str
    email = str

    def convert_into_domain(self, dto: dict):
        self.id = dto.get("id")
        self.name = dto.get("name")
        self.surname = dto.get("surname")
        self.phone = dto.get("phone")
        self.email = dto.get("email")

        return self


@dataclass
class Note:
    id = int
    customer_id = int
    note = str

    def convert_into_domain(self, dto: dict):
        self.id = dto.get("id")
        self.customer_id = dto.get("customer_id")
        self.note = dto.get("note")

        return self
