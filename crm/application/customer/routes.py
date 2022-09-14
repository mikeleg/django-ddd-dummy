from .views import CustomerApiViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"customer", CustomerApiViewSet, basename="customer"),
