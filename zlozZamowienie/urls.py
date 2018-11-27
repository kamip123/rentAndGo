from django.urls import path
from . import views

urlpatterns = [
    path('<int:idOferty>/', views.zloz_zamowienie, name='zloz_zamowienie'),
]
