from typing import Protocol

from domain.entities.customer import Customer


class ICustomerRepository(Protocol):
    def retrieve_all_customers(self) -> list[Customer]:
        ...

    def retrive_customer(self, customer_id) -> Customer:
        ...
