from http.client import BAD_REQUEST, OK

from core.domain.entities.customer import Customer
from data.repositories.customer import CustomerRepository
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from .dto import CustomerCreateRequestDto, CustomerResponseDto, CustomerUpdateRequestDto
from .services import CustomerService


class CustomerApiViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        repo = CustomerRepository()
        self.service = CustomerService(repo)

    @extend_schema(
        responses=CustomerResponseDto,
    )
    def list(self, request):
        customers = self.service.all()

        return Response(CustomerResponseDto(customers, many=True).data, status=OK)

    @extend_schema(
        responses=CustomerResponseDto,
    )
    def retrieve(self, request, pk: int):
        customer = self.service.detail(pk)

        if customer is None:
            return Response(None, status=OK)

        return Response(CustomerResponseDto(customer).data, status=OK)

    @extend_schema(
        request=CustomerCreateRequestDto,
        responses=CustomerResponseDto,
    )
    def create(self, request):

        dto = CustomerCreateRequestDto(data=request.data)
        if not dto.is_valid():
            return Response(dto.error_messages, status=BAD_REQUEST)

        customer_new = self.service.add(Customer.convert_to_entity(dto.data))
        return Response(CustomerResponseDto(customer_new).data, status=OK)

    @extend_schema(
        request=CustomerUpdateRequestDto,
        responses=CustomerResponseDto,
    )
    def update(self, request, pk: int):
        dto = CustomerUpdateRequestDto(data=request.data)

        if not dto.is_valid():
            return Response(dto.error_messages, status=BAD_REQUEST)

        customer_new = self.service.update(Customer.convert_to_entity(dto.data))
        return Response(CustomerResponseDto(customer_new).data, status=OK)

    @extend_schema()
    def destroy(self, request, pk=None):
        self.service.delete(pk)
        return Response(None, status=OK)
