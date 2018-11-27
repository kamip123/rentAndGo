from django.shortcuts import render

# Create your views here.


def informacje(request):
    return render(request, 'informacje.html')
