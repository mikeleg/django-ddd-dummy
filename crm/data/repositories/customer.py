from typing import Optional
from data.interfaces.customer import ICustomerRepository
from data import models
from core.domain.entities.customer import Customer

from django.forms.models import model_to_dict


class CustomerRepository(ICustomerRepository):
    def all(self) -> list[Customer]:
        customers = models.Customer.objects.all()

        if not customers.exists():
            return []

        return [
            Customer.convert_to_entity(model_to_dict(customer))
            for customer in customers
        ]

    def get_by_id(self, customer_id: int) -> Optional[Customer]:
        customer = models.Customer.objects.filter(id=customer_id)

        if not customer.exists():
            return None

        return Customer.convert_to_entity(model_to_dict(customer.first()))

    def add(self, customer: Customer) -> Customer:
        new_db_customer = models.Customer(**customer.__dict__)
        new_db_customer.save()

        return Customer().convert_into_domain(new_db_customer)

    def update(self, customer: Customer) -> Customer:
        models.Customer.objects.filter(id=customer.id).update(**customer.__dict__)

        return Customer.convert_to_entity(model_to_dict(customer))

    def delete(self, customer_id) -> None:
        models.Customer.objects.filter(id=customer_id).delete()
