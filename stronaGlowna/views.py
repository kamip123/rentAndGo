from django.shortcuts import render, redirect
from .models import Komentarz, OfertyStronaGlownaOsobowe, OfertyStronaGlownaWieksze
# Create your views here.


def strona_glowna(request):
    if request.method == 'POST':
        if 'SearchForm' in request.POST:
            odbior = request.GET.get('reception')
            odbior_godzina = request.GET.get('receptiont')
            odbior_minuta = request.GET.get('receptiontt')
            request.session['odbior'] = odbior
            request.session['odbior_godzina'] = odbior_godzina
            request.session['odbior_minuta'] = odbior_minuta

            oddanie = request.GET.get('reception')
            oddanie_godzina = request.GET.get('receptiont')
            oddanie_minuta = request.GET.get('receptiontt')
            request.session['oddanie'] = oddanie
            request.session['oddanie_godzina'] = oddanie_godzina
            request.session['oddanie_minuta'] = oddanie_minuta

            return redirect('oferty/')

    komentarz1 = Komentarz.objects.get(id=1)
    komentarz2 = Komentarz.objects.get(id=2)
    komentarz3 = Komentarz.objects.get(id=3)
    komentarz4 = Komentarz.objects.get(id=4)
    oferty1 = OfertyStronaGlownaOsobowe.objects.get(id=1)
    oferty2 = OfertyStronaGlownaWieksze.objects.get(id=1)
    return render(request, 'stronaGlowna.html',
                  {'komentarz1': komentarz1, 'komentarz2': komentarz2, 'komentarz3': komentarz3,
                   'komentarz4': komentarz4, 'oferty1': oferty1, 'oferty2': oferty2})
