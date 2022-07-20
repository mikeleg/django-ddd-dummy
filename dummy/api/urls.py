from django.urls import path, include
from rest_framework import routers
from .views import DummyViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"dummy", DummyViewSet, basename="dummy")
urlpatterns = router.urls


urlpatterns = [
    path("", include(router.urls)),
]
