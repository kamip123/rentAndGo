from django.urls import path
from . import views

urlpatterns = [
    path('', views.wyloguj, name='wyloguj'),
]