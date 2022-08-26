from rest_framework import viewsets
from rest_framework.response import Response

from services import CustomerService
from .dto import CustomerResponseDto
from data.repositories import CustomerRepository


class CustomerApiViewSet(viewsets.ViewSet):
    def __init__(self):
        self.repo = CustomerRepository()
        self.service = CustomerService(self.repo)

    def list(self, request):

        customers = self.service.retrive_all_customers()

        return Response(CustomerResponseDto(data=customers).data)

    def retrieve(self, request, pk=None):
        customer = self.service.retrieve_customer(pk)

        return Response(CustomerResponseDto(data=customer).data)
