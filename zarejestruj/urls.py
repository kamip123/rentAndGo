from django.urls import path
from . import views

urlpatterns = [
    path('', views.zarejestruj, name='zarejestruj'),
]