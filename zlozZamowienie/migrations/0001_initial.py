# Generated by Django 2.1.2 on 2018-11-27 00:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oferty', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dodadek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(default='GPS', max_length=50)),
                ('cena', models.FloatField(default=20, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Ubezpieczenie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena', models.FloatField(default=200, max_length=20)),
                ('nazwa', models.CharField(default='Pokryjemy wszystkie straty', max_length=50)),
                ('procent', models.FloatField(default=90, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_kiedy', models.DateTimeField(blank=True, null=True)),
                ('do_zaplaty', models.FloatField(default=200, max_length=20)),
                ('kaucja', models.FloatField(default=200, max_length=20)),
                ('do_kiedy', models.DateTimeField(blank=True, null=True)),
                ('data_zamowienia', models.DateTimeField(default=django.utils.timezone.now)),
                ('dodatki', models.ManyToManyField(blank=True, null=True, to='zlozZamowienie.Dodadek')),
                ('id_samochodu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='oferty.Samochod')),
                ('id_ubezpieczenia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='zlozZamowienie.Ubezpieczenie')),
                ('kupujacy', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
