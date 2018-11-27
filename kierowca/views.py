from django.shortcuts import render

# Create your views here.


def kierowca(request):
    return render(request, 'kierowca.html')
