from typing import Optional, Protocol
from domain.entities.customer import Customer


class ICustomerRepository(Protocol):
    def all(self) -> list[Customer]:
        ...

    def get_by_id(self, customer_id) -> Optional[Customer]:
        ...

    def add(self, customer) -> Customer:
        ...

    def update(self, customer) -> Customer:
        ...

    def delete(self, customer_id) -> None:
        ...
