from rest_framework import serializers
from .models import Currency, CurrencyConversionRates


class CurrencySerializer(serializers.ModelSerializer):
    """
    Serializer class for Currency model, which inherits from the ModelSerializer class
    """

    class Meta:
        model = Currency
        fields = ["name", "symbol"]


class CurrencyConversionRatesSerializer(serializers.ModelSerializer):
    """
    Serializer class for CurrencyConversionRates model, which inherits from the ModelSerializer class
    """

    class Meta:
        model = CurrencyConversionRates
        fields = ["from_currency", "to_currency", "rate", "date"]
