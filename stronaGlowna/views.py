from django.shortcuts import render
from .models import Komentarz
# Create your views here.


def strona_glowna(request):
    komentarz1 = Komentarz.objects.get(id=1)
    komentarz2 = Komentarz.objects.get(id=2)
    komentarz3 = Komentarz.objects.get(id=3)
    komentarz4 = Komentarz.objects.get(id=4)
    return render(request, 'stronaGlowna.html', {'komentarz1': komentarz1, 'komentarz2': komentarz2, 'komentarz3': komentarz3, 'komentarz4': komentarz4})
