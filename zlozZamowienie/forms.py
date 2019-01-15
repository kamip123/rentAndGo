from django import forms

from .models import Zamowienie


class ZlozZamowienie(forms.ModelForm):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
    )

    ubezpieczenie = forms.ChoiceField(label="", initial='', widget=forms.Select, choices=CHOICES, required=True)

    class Meta:
        model = Zamowienie
        fields = ['od_kiedy', 'do_kiedy', 'dodatki']
        widgets = {
            'od_kiedy': forms.DateInput(attrs={'class': 'dateinput1'}),
            'do_kiedy': forms.DateInput(attrs={'class': 'dateinput2'}),
            'dodatki': forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple)
        }
