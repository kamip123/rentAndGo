# Generated by Django 2.1.2 on 2018-12-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nr_telefonu',
            field=models.CharField(default='+48854125894', max_length=12),
        ),
    ]
