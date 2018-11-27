from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
# Create your views here.


def zaloguj(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('../zamowienia/')
        else:
            return render(request, 'zaloguj.html', {'form': form})
    else:
        return render(request, 'zaloguj.html', {'form': form})
