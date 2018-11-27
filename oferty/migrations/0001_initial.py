# Generated by Django 2.1.2 on 2018-11-27 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Samochod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cena', models.FloatField(max_length=20)),
                ('czy_dostepny', models.BooleanField(default=True)),
                ('marka', models.CharField(default='Maluch', max_length=50)),
                ('nr_rejestracyjny', models.CharField(default='GD XXXX', max_length=50)),
                ('przebieg', models.FloatField(default=1, max_length=20)),
                ('rodzaj_paliwa', models.IntegerField(default=1)),
                ('spalanie', models.FloatField(default=8, max_length=20)),
                ('typ', models.CharField(default='Osobowe', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wypozyczalnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lokalizacja', models.CharField(default='Gdansk', max_length=100)),
                ('nazwa', models.CharField(default='Najlepsza', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='samochod',
            name='id_wypozyczalni',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oferty.Wypozyczalnia'),
        ),
    ]
