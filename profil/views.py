from django.shortcuts import render, redirect
from .forms import EditEmailForm, EditProfileForm, EditNamesForm
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


def profile_page(request):
    user = request.user
    profil = Profile.objects.get(user=user)
    return render(request, 'indexProfileUser.html', {'user': user, 'profil': profil})


def haslo_page(request):
    alert = 0
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            form = PasswordChangeForm(user=request.user)
            alert = 1
            return redirect('../../')
        return render(request, 'passwordProfileUser.html', {'form': form, 'alert': alert})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'passwordProfileUser.html', {'form': form, 'alert': alert})


def email_page(request):
    if request.method == 'POST':
        form = EditEmailForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditEmailForm(instance=request.user)
            alert = 1

        return render(request, 'emailProfileUser.html', {'form': form, 'alert': alert})
    form = EditEmailForm(instance=request.user)
    return render(request, 'emailProfileUser.html', {'form': form})


def profilowe_page(request):
    profil = Profile.objects.get(user=request.user)
    form = EditProfileForm(instance=profil)
    form2 = EditNamesForm(instance=request.user)

    if request.method == 'POST':
        if 'profilChangeForm' in request.POST:
            profil = Profile.objects.get(user=request.user)
            form = EditProfileForm(request.POST, request.FILES, instance=profil)
            if form.is_valid():
                form.save()
                return render(request, 'profileProfileUser.html', {'form2': form2, 'form': form, 'profil': profil})
        elif 'namesChangeForm' in request.POST:
            profil = Profile.objects.get(user=request.user)
            form2 = EditNamesForm(request.POST, request.FILES, instance=request.user)
            if form2.is_valid():
                form2.save()
                return render(request, 'profileProfileUser.html', {'form2': form2, 'form': form, 'profil': profil})

    return render(request, 'profileProfileUser.html', {'form2': form2, 'form': form, 'profil': profil})
