from django.shortcuts import render
from zlozZamowienie.models import Zamowienie
# Create your views here.


def zamowienia(request):
    zamowieniaa = Zamowienie.objects.filter(kupujacy=request.user).order_by('data_zamowienia')
    return render(request, 'zamowienia.html', {'zamowienia': zamowieniaa})


def zamowienie(request, idZamowienia):
    zamowieniee = Zamowienie.objects.get(id=idZamowienia)
    return render(request, 'zamowienie.html', {'zamowienie': zamowieniee})
