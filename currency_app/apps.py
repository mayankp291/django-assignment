from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate

class CurrencyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency_app'
