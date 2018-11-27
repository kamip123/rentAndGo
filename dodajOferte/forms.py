from django import forms
from oferty.models import Samochod


class DodajOferte(forms.ModelForm):
    class Meta:
        model = Samochod
        fields = '__all__'
