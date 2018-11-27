from django.shortcuts import render
from .models import Samochod
# Create your views here.


def oferty(request):
    ofertyy = Samochod.objects.all()
    return render(request, 'oferty.html', {'oferty': ofertyy})


def oferta(request, idOferty):
    ofertaa = Samochod.objects.get(id=idOferty)
    return render(request, 'oferta.html', {'oferta': ofertaa})
