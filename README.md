# django-assignment

## APIs

### GET /currency/?filter={string}
Returns a list of currencies in the database. The data can be filtered using the "filter" query param. The data returned in sorted in ascending order.

### Response
```
{
    "data": {
        "status": "success",
        "message": "Currencies fetched successfully",
        "data": [
            "Australian Dollar (AUD)",
            "Brazilian Real (BRL)",
            "British Pound (GBP)",
            "Bulgarian Lev (BGN)",
            "Canadian Dollar (CAD)",
            "Chinese Renminbi Yuan (CNY)",
            "Czech Koruna (CZK)",
            "Danish Krone (DKK)",
            "Euro (EUR)",
            "Hong Kong Dollar (HKD)",
            "Hungarian Forint (HUF)",
            "Icelandic Króna (ISK)",
            "Indian Rupee (INR)",
            "Indonesian Rupiah (IDR)",
            "Israeli New Sheqel (ILS)",
            "Japanese Yen (JPY)",
            "Malaysian Ringgit (MYR)",
            "Mexican Peso (MXN)",
            "New Zealand Dollar (NZD)",
            "Norwegian Krone (NOK)",
            "Philippine Peso (PHP)",
            "Polish Złoty (PLN)",
            "Romanian Leu (RON)",
            "Singapore Dollar (SGD)",
            "South African Rand (ZAR)",
            "South Korean Won (KRW)",
            "Swedish Krona (SEK)",
            "Swiss Franc (CHF)",
            "Thai Baht (THB)",
            "Turkish Lira (TRY)",
            "United States Dollar (USD)"
        ],
        "count": 31
    }
}
```

## POST /currency/ (test purposes)

Add a new currency. Does not create if the currency already exists.

### Request
```
Body: 
{
    "name": "Test Currency",
    "symbol": "TCU"
}
```
### Response
```
{
    "data": {
        "status": "success",
        "message": "Currency created successfully",
        "data": {
            "name": "Test Currency",
            "symbol": "TCU"
        }
    }
}
```

## POST /load-currencies (initialise db)
The request is use to fetch the currencies and (or) the historical rates for the currencies.

### Request
```
Body: 
{
    "load_historical_data": true,  
    "historical_from_date": "2023-01-01",
    "historical_to_date": "2024-04-12"
}   
```
### Response
```
{
    "data": {
        "status": "success",
        "message": "Currencies loaded successfully"
    }
}
```

## Admin Panel

### A view of Currency Model
![image](https://github.com/mayankp291/django-assignment/assets/69447074/a8a864a2-2400-496a-bdb0-64642386e704)


### A view of Currency Conversion Rates Model
Filtered by USD/SGD rates
![image](https://github.com/mayankp291/django-assignment/assets/69447074/a0a9de01-ca60-49e9-b57c-d17bc725c3a4)



## Forex Data

The forex data used is provided from [Frankfurter API](https://www.frankfurter.app/), which is an exchange rates and conversion API for currency data published by the European Central Bank. I used this over Yahoo Finance as more currencies were available and it allowed me to get rates between any 2 currencies.
