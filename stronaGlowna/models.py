from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Komentarz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=200)
    komentarz = models.TextField()
