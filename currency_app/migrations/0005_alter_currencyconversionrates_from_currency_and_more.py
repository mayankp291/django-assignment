# Generated by Django 5.0.4 on 2024-04-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_app', '0004_currencyconversionrates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyconversionrates',
            name='from_currency',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='currencyconversionrates',
            name='to_currency',
            field=models.CharField(max_length=3),
        ),
    ]
