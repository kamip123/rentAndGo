"""rentandgo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stronaGlowna.urls')),
    path('oferty/', include('oferty.urls')),
    path('kierowca/', include('kierowca.urls')),
    path('informacje/', include('informacje.urls')),
    path('kontakt/', include('kontakt.urls')),
    path('zaloguj/', include('zaloguj.urls')),
    path('zarejestruj/', include('zarejestruj.urls')),
    path('dodajOferte/', include('dodajOferte.urls')),
    path('zlozZamowienie/', include('zlozZamowienie.urls')),
    path('zamowienia/', include('zamowienia.urls')),
    path('wyloguj/', include('wyloguj.urls')),
    path('profil/', include('profil.urls')),
    path('api/', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
