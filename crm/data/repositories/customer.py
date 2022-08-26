from crm.data.interfaces.customer import ICustomerRepository
from crm.data.models import CustomerModel
from crm.domain.entities.customer import Customer
from data.interfaces.customer import ICustomerRepository


class CustomerRepository(ICustomerRepository):
    def __init__(self):
        self.db = CustomerModel()

    def retrieve_all_customers(self) -> list[Customer]:
        return self.db.objects.all()

    def retrive_customer(self, customer_id) -> Customer:
        return self.db.objects.get(id=customer_id)
