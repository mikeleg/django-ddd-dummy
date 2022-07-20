from rest_framework import viewsets, status
from .repository.dummy_repository import DummyRepository

from .serializers.dummy import DummyResponseSerializer
from rest_framework.response import Response


class DummyViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs) -> None:
        self.repo = DummyRepository()
        super().__init__(**kwargs)

    def list(self, request):
        serializer = DummyResponseSerializer(self.repo.get_dummy_list(), many=True)

        if not serializer.is_valid:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)

    def retrieve(self, request, pk: int = None):
        serializer = DummyResponseSerializer(self.repo.get_dummy_by_id(pk), many=True)

        if not serializer.is_valid:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)
