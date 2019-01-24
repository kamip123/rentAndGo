from django import forms

from .models import Zamowienie, Dodadek


class ZlozZamowienie(forms.ModelForm):
    CHOICES = (
        (1, 'Podstawowe'),
        (2, 'Middle'),
        (3, 'All risks'),
    )

    ubezpieczenie = forms.ChoiceField(label="", initial='', widget=forms.Select, choices=CHOICES, required=True)
    dodatki = forms.ModelMultipleChoiceField(queryset=Dodadek.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Zamowienie
        fields = ['od_kiedy', 'do_kiedy']
        widgets = {
            'od_kiedy': forms.DateInput(attrs={'class': 'dateinput1'}),
            'do_kiedy': forms.DateInput(attrs={'class': 'dateinput2'}),
        }
