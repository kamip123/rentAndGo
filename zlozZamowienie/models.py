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


class Kierowca(models.Model):
    nazwisko = models.OneToOneField(User, on_delete=models.CASCADE)
    imię = nr_dowodu = models.CharField(max_length=18)
    nr_dowodu = models.CharField(max_length=12, default=446546546)
    nr_prawa_jazdy = models.CharField(max_length=12, default=446546546)
    nr_telefonu = models.CharField(max_length=12, default="+48854125894")


class Zamowienie(models.Model):
    od_kiedy = models.DateTimeField()
    do_kiedy = models.DateTimeField()
    dodatki = models.ManyToManyField(Dodadek, blank=True, null=True)
    id_ubezpieczenia = models.ForeignKey(Ubezpieczenie, on_delete=models.CASCADE)
    do_zaplaty = models.FloatField(max_length=20, default=200)
    id_samochodu = models.ForeignKey(Samochod, on_delete=models.CASCADE)
    kupujacy = models.ForeignKey(User, on_delete=models.CASCADE)
    kaucja = models.FloatField(max_length=20, default=200)
    data_zamowienia = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.kupujacy.username
