from rest_framework import routers
from oferty.viewsets import SamochodViewSet

router = routers.DefaultRouter()
router.register(r'samochod', SamochodViewSet)