from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


def zarejestruj(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('../oferty/')
        else:
            return render(request, 'zarejestruj.html', {'form': form})
    else:
        return render(request, 'zarejestruj.html', {'form': form})
