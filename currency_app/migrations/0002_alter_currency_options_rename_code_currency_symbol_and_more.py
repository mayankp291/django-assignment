# Generated by Django 5.0.4 on 2024-04-14 14:04

import django.utils.timezone
import django_extensions.db.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': ['name'], 'verbose_name': 'Currency', 'verbose_name_plural': 'Currencies'},
        ),
        migrations.RenameField(
            model_name='currency',
            old_name='code',
            new_name='symbol',
        ),
        migrations.AddField(
            model_name='currency',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
        migrations.AlterField(
            model_name='currency',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
