from django.shortcuts import render, redirect
from oferty.models import Samochod
from .forms import ZlozZamowienie
# Create your views here.


def zloz_zamowienie(request, idOferty):
    ofertaa = Samochod.objects.get(id=idOferty)
    zamowienie = ZlozZamowienie()
    if request.method == 'POST':
        zamowienie = ZlozZamowienie(request.POST)
        if zamowienie.is_valid():
            zamowienie.save()
            return redirect('../zlozZamowienie/')
        else:
            return render(request, 'dodajOferte.html', {'oferta': ofertaa, 'zamowienie': zamowienie})
    return render(request, 'zlozZamowienie.html', {'oferta': ofertaa, 'zamowienie': zamowienie})
