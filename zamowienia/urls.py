from django.urls import path
from . import views

urlpatterns = [
    path('', views.zamowienia, name='zamowienia'),
    path('<int:idZamowienia>/', views.zamowienie, name='zamowienie'),
]
