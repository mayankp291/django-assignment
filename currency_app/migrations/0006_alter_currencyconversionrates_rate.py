# Generated by Django 5.0.4 on 2024-04-14 16:56

import currency_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_app', '0005_alter_currencyconversionrates_from_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyconversionrates',
            name='rate',
            field=models.DecimalField(decimal_places=5, max_digits=20, validators=[currency_app.models.validate_positive_rate]),
        ),
    ]
