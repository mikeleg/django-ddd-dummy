from typing import Optional
from data.interfaces.customer import ICustomerRepository
from data.models import CustomerModel
from domain.entities.customer import Customer
from django.core.exceptions import ObjectDoesNotExist


class CustomerRepository(ICustomerRepository):
    def all(self) -> list[Customer]:
        customers = CustomerModel.objects.all()

        if len(customers) == 0:
            return []

        return list(
            [
                Customer().convert_into_domain(customer.__dict__)
                for customer in customers
            ]
        )

    def get_by_id(self, customer_id: int) -> Optional[Customer]:
        result: Customer = None
        try:
            customer = CustomerModel.objects.get(id=customer_id)
            result = Customer().convert_into_domain(customer.__dict__)
        except ObjectDoesNotExist:
            ...

        return result

    def add(self, customer: Customer) -> Customer:
        new_db_customer = CustomerModel(**customer.__dict__)
        new_db_customer.save()

        return Customer().convert_into_domain(new_db_customer.__dict__)

    def update(self, customer: Customer) -> Customer:
        CustomerModel.objects.filter(id=customer.id).update(**customer.__dict__)

        return Customer().convert_into_domain(customer.__dict__)

    def delete(self, customer_id) -> None:
        CustomerModel.objects.filter(id=customer_id).delete()
