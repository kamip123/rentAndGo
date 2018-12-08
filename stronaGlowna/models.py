from django.db import models
from django.contrib.auth.models import User
from oferty.models import Samochod


class Komentarz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=200)
    komentarz = models.TextField()


class OfertyStronaGlownaOsobowe(models.Model):
    samochody = models.ManyToManyField(Samochod)


class OfertyStronaGlownaWieksze(models.Model):
    samochody = models.ManyToManyField(Samochod)
