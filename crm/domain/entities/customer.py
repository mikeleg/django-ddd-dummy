from dataclasses import dataclass
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Customer:
    id = int
    name = str
    surname = str
    phone = str
    email = str

    def convert_into_domain(self, dto):
        self.id = dto["id"] if "id" in dto else None
        self.name = dto["name"] if "name" in dto else None
        self.surname = dto["surname"] if "surname" in dto else None
        self.phone = dto["phone"] if "phone" in dto else None
        self.email = dto["email"] if "email" in dto else None

        return self
