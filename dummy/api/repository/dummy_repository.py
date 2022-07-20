from typing import Protocol

from db import models
from domain.entities import dummy


class IDummyRepository(Protocol):
    def get_dummy_by_id(self, id: int) -> dummy.Dummy:
        pass

    def get_dummy_list(self) -> list[dummy.Dummy]:
        pass


class DummyRepository(IDummyRepository):
    def get_dummy_by_id(self, id: int) -> dummy.Dummy:
        if id is None:
            raise Exception("id is None")

        return models.Dummy.objects.get(id=id).values(
            "id", "name", "surname", "age", "address", "created_at", "updated_at"
        )

    def get_dummy_list(self) -> list[dummy.Dummy]:
        return list(
            models.Dummy.objects.all().values_list(
                "id", "name", "surname", "age", "address", "created_at", "updated_at"
            )
        )
