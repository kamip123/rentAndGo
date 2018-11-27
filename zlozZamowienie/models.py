from django.db import models
from oferty.models import Samochod
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Dodadek(models.Model):
    nazwa = models.CharField(max_length=50, default="GPS")
    cena = models.FloatField(max_length=20, default=20)

    def __str__(self):
        return self.nazwa


class Ubezpieczenie(models.Model):
    cena = models.FloatField(max_length=20, default=200)
    nazwa = models.CharField(max_length=50, default="Pokryjemy wszystkie straty")
    procent = models.FloatField(max_length=20, default=90)


class Zamowienie(models.Model):
    od_kiedy = models.DateTimeField(blank=True, null=True)
    do_zaplaty = models.FloatField(max_length=20, default=200)
    dodatki = models.ManyToManyField(Dodadek, blank=True)
    id_samochodu = models.ForeignKey(Samochod, on_delete=models.CASCADE)
    id_ubezpieczenia = models.ForeignKey(Ubezpieczenie, on_delete=models.CASCADE)
    kupujacy = models.ForeignKey(User, on_delete=models.CASCADE)
    kaucja = models.FloatField(max_length=20, default=200)
    do_kiedy = models.DateTimeField(blank=True, null=True)
    data_zamowienia = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.kupujacy.username
