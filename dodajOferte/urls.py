from django.urls import path
from . import views

urlpatterns = [
    path('', views.dodaj_oferte, name='dodaj_oferte'),
]
