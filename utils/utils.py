import requests
from currency_app.models import Currency, CurrencyConversionRates
from currency_app.serializers import (
    CurrencySerializer,
    CurrencyConversionRatesSerializer,
)
from concurrent.futures import ThreadPoolExecutor


def fetch_and_store_currencies():
    """
    Fetches currencies from the API and stores it in the Currency database
    """
    url = "https://api.frankfurter.app/currencies"
    response = requests.get(url)
    data = response.json()

    # Clear existing data in the Currency model
    Currency.objects.all().delete()

    # Store new currency data in the database
    for symbol, name in data.items():
        serializer = CurrencySerializer(data={"symbol": symbol, "name": name})
        if serializer.is_valid():
            serializer.save()
            print(f"Currency {name} with code {symbol} saved successfully")


def populate_exchange_rates(historical_from_date: str, historical_to_date: str):
    """
    Fetches historical exchange rates from the API and stores it in the CurrencyConversionRates database
    """
    # get all symbols from db
    currencies = Currency.objects.all()
    symbols = {currency.symbol for currency in currencies}
    print(symbols)
    CurrencyConversionRates.objects.all().delete()

    # define a function to fetch data and process it
    def fetch_and_process(from_curr: str):
        if historical_from_date and historical_to_date:
            url = f"https://api.frankfurter.app/{historical_from_date}..{historical_to_date}?from={from_curr}"
        else:
            url = f"https://api.frankfurter.app/2024-01-01..?from={from_curr}"
        response = requests.get(url)
        data = response.json()
        process_json(data)

    # execute fetch_and_process function concurrently
    with ThreadPoolExecutor() as executor:
        executor.map(fetch_and_process, symbols)


def process_json(data):
    """
    Process the JSON data with all rates and store it in the CurrencyConversionRates database
    """
    from_curr = data["base"]
    rates = data["rates"]
    for date in rates:
        for to_curr in rates[date]:
            rate = rates[date][to_curr]
            # make rate 5 decimal places max
            rate = round(rate, 5)
            serializer = CurrencyConversionRatesSerializer(
                data={
                    "from_currency": from_curr,
                    "to_currency": to_curr,
                    "rate": rate,
                    "date": date,
                }
            )
            if serializer.is_valid():
                serializer.save()
                print(f"{from_curr} to {to_curr} on {date} is {rate}")
            else:
                print("Validation Error:", serializer.errors)
