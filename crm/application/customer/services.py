from typing import Optional, Protocol
from data.repositories.customer import CustomerRepository
from core.domain.entities.customer import Customer


class ICustomerService(Protocol):
    def all(self) -> list[Customer]:
        ...

    def detail(self, customer_id: int) -> Optional[Customer]:
        ...

    def add(self, customer: Customer) -> Customer:
        ...

    def update(self, customer: Customer) -> Customer:
        ...

    def delete(self, customer_id) -> None:
        ...


class CustomerService(ICustomerService):
    def __init__(self, repo: CustomerRepository) -> None:
        self.repo = repo

    def all(self) -> list[Customer]:
        return self.repo.all()

    def detail(self, customer_id) -> Optional[Customer]:
        return self.repo.get_by_id(customer_id)

    def add(self, new_customer: Customer) -> Customer:
        return self.repo.add(new_customer)

    def update(self, updated_customer: Customer) -> Customer:
        return self.repo.update(updated_customer)

    def delete(self, customer_id) -> None:
        return self.repo.delete(customer_id)
