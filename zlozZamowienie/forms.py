from django import forms
from .models import Zamowienie


class ZlozZamowienie(forms.ModelForm):
    class Meta:
        model = Zamowienie
        fields = '__all__'
