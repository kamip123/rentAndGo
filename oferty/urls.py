from django.urls import path
from . import views

urlpatterns = [
    path('', views.oferty, name='oferty'),
    path('<int:idOferty>/', views.oferta, name='oferta'),
]