from crm.data.interfaces.customer import ICustomerRepository
from crm.domain.entities.customer import Customer


class CustomerService:
    def __init__(self, repo: ICustomerRepository) -> None:
        self.repo = repo

    def retrive_all_customers(self) -> list[Customer]:
        return self.repo.retrieve_all_customers()

    def retrieve_customer(self, customer_id) -> Customer:
        return self.repo.retrieve_customer(customer_id)
