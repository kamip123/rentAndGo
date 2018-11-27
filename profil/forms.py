from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Profile


class EditEmailForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'email'
        }


class EditNamesForm(UserChangeForm):

    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name'
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {
            'nr_dowodu',
            'nr_prawa_jazdy',
            'nr_telefonu'
        }
