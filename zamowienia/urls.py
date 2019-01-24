from django.urls import path
from . import views

app_name = 'zamowienia'

urlpatterns = [
    path('', views.zamowienia, name='zamowienia'),
    path('<int:idZamowienia>/', views.zamowienie, name='zamowienie'),
    path('platnosc/<int:idZamowienia>/', views.payment_process, name='process'),
    path('platnosc/<int:payment_id>/done/', views.payment_done, name='done'),
    path('platnosc/<int:payment_id>/canceled/', views.payment_canceled, name='canceled'),
]
