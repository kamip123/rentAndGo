from rest_framework import serializers
from .models import Samochod


class SamochodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Samochod
        fields = '__all__'
