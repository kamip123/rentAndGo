from django.shortcuts import render, redirect
from django.utils import timezone
from oferty.models import Samochod
from zlozZamowienie.models import Ubezpieczenie
from .forms import ZlozZamowienie
# Create your views here.


def zloz_zamowienie(request, idOferty):
    ofertaa = Samochod.objects.get(id=idOferty)
    if request.user.is_authenticated:
        zamowienie = ZlozZamowienie()
        if request.method == 'POST':
            zamowienie = ZlozZamowienie(request.POST)
            if zamowienie.is_valid():
                zamowieniee = zamowienie.save(commit=False)
                zamowieniee.do_zaplaty = ofertaa.cena
                zamowieniee.id_samochodu = ofertaa
                zamowieniee.kupujacy = request.user
                zamowieniee.kaucja = ofertaa.cena * 2
                zamowieniee.data_zamowienia = timezone.now()
                zamowieniee.id_ubezpieczenia = Ubezpieczenie.objects.get(id=zamowienie.cleaned_data['ubezpieczenie'])
                zamowieniee.save()
                zamowienie.save_m2m()
                return redirect('../../../../zamowienia/')
            else:
                return render(request, 'zlozZamowienie.html', {'oferta': ofertaa, 'zamowienie': zamowienie})
        return render(request, 'zlozZamowienie.html', {'oferta': ofertaa, 'zamowienie': zamowienie})
    else:
        ofertaa = None
        zamowienie = None
        return render(request, 'zlozZamowienie.html', {'oferta': ofertaa, 'zamowienie': zamowienie})