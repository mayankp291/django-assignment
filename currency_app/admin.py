from django.contrib import admin
from . import models


@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    """
    Admin class for Currency model
    """

    list_display = ["name", "symbol"]
    search_fields = ["name", "symbol"]
    list_filter = ["name", "symbol"]


@admin.register(models.CurrencyConversionRates)
class CurrencyConversionRatesAdmin(admin.ModelAdmin):
    """
    Admin class for CurrencyConversionRates model
    """

    list_display = ["from_currency", "to_currency", "rate", "date"]
    search_fields = ["from_currency", "to_currency", "rate", "date"]
    list_filter = ["from_currency", "to_currency", "date"]
