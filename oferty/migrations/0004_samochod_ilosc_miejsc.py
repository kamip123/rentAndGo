# Generated by Django 2.1.2 on 2018-12-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oferty', '0003_auto_20181127_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='samochod',
            name='ilosc_miejsc',
            field=models.IntegerField(default=5),
        ),
    ]
