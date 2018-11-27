from rest_framework import viewsets
from .models import Samochod
from .serializers import SamochodSerializer


class SamochodViewSet(viewsets.ModelViewSet):
    queryset = Samochod.objects.all()
    serializer_class = SamochodSerializer
















