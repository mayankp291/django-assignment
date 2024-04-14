from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from utils.model_abstracts import Model
from django_extensions.db.models import (
    TimeStampedModel,
)


def validate_positive_rate(value):
    if value <= 0:
        raise ValidationError("Rate must be a positive number.")


class Currency(TimeStampedModel, Model):
    """
    Represents a currency with a unique name and symbol.

    Attributes:
    - name: A unique name for the currency (e.g., "US Dollar").
    - symbol: A unique symbol for the currency (e.g., "USD").

    Meta:
    - verbose_name: "Currency"
    - verbose_name_plural: "Currencies"
    - ordering: Currencies are ordered by their name.
    """

    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class CurrencyConversionRates(TimeStampedModel, Model):
    """
    Represents a currency conversion rate between two currencies.

    Attributes:
    - from_currency: The currency being converted from (e.g., "USD").
    - to_currency: The currency being converted to (e.g., "EUR").
    - rate: The conversion rate from the from_currency to the to_currency.
    - date: The date when the conversion rate was recorded.

    Meta:
    - verbose_name: "Currency Conversion Rate"
    - verbose_name_plural: "Currency Conversion Rates"
    - ordering: Rates are ordered by their date in descending order.
    """

    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    rate = models.DecimalField(
        max_digits=20, decimal_places=5, validators=[validate_positive_rate]
    )
    date = models.DateField()

    class Meta:
        verbose_name = "Currency Conversion Rate"
        verbose_name_plural = "Currency Conversion Rates"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.from_currency} to {self.to_currency} rate: {self.rate}"
