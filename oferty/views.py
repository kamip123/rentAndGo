from django.shortcuts import render, redirect

from zlozZamowienie.views import zloz_zamowienie
from .models import Samochod
# Create your views here.


def oferty(request):
    ofertyy = Samochod.objects.all()
    return render(request, 'oferty.html', {'oferty': ofertyy})


def oferta(request, idOferty):
    return redirect('zloz_zamowienie', idOferty=idOferty)
