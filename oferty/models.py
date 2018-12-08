from django.db import models

# Create your models here.


class Wypozyczalnia(models.Model):
    lokalizacja = models.CharField(max_length=100, default="Gdansk")
    nazwa = models.CharField(max_length=50, default="Najlepsza")
    adres = models.CharField(max_length=100, default="Lotnisko")

    def __str__(self):
        return self.nazwa


class Samochod(models.Model):
    cena = models.FloatField(max_length=20)
    czy_dostepny = models.BooleanField(default=True)
    id_wypozyczalni = models.ForeignKey(Wypozyczalnia, on_delete=models.CASCADE)
    marka = models.CharField(max_length=50, default="Maluch")
    nr_rejestracyjny = models.CharField(max_length=50, default="GD XXXX")
    przebieg = models.FloatField(max_length=20, default=1)
    rodzaj_paliwa = models.CharField(max_length=50, default="Ropa")
    spalanie = models.FloatField(max_length=20, default=8)
    typ = models.CharField(max_length=50, default="Osobowe")
    ilosc_miejsc = models.IntegerField(default=5)

    def __str__(self):
        return self.marka

