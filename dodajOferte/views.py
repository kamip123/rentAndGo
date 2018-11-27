from django.shortcuts import render
from .forms import DodajOferte
# Create your views here.


def dodaj_oferte(request):
    oferta = DodajOferte()
    if request.method == 'POST':
        oferta = DodajOferte(request.POST)
        if oferta.is_valid():
            oferta.save()
            oferta = DodajOferte()
            return render(request, 'dodajOferte.html', {'oferta': oferta})
        else:
            return render(request, 'dodajOferte.html', {'oferta': oferta})
    return render(request, 'dodajOferte.html', {'oferta': oferta})
