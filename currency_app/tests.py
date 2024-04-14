from .models import Currency, CurrencyConversionRates
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status

class TestCurrencyApi(APITestCase):
    """	
    Test cases for the Currency API
    """
    def setUp(self):
        self.client = APIClient()
        self.currency_url = "/currency/"
        self.load_currencies_url = "/load-currencies/"
        self.data = {
            "name": "Singapore Dollar",
            "symbol": "SGD",
        }
        self.load_currencies_data = {
            "load_historical_data": False,  
            "historical_from_date": "2024-04-12",
            "historical_to_date": "2024-04-12",
        }       
    
    def test_create_currency(self):
        """
        Test case to add a new currency
        """
        response = self.client.post(self.currency_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Currency.objects.count(), 1)
        self.assertEqual(Currency.objects.get().symbol, "SGD")
    
    def test_create_currency_with_invalid_data(self):
        """
        Test case to add a new currency with invalid data
        """
        data = self.data
        data.pop("name")
        response = self.client.post(self.currency_url, {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Currency.objects.count(), 0)
    
    def test_unique_of_currency_symbol(self):
        """
        Test case to check uniqueness of currency symbol
        """
        response = self.client.post(self.currency_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post(self.currency_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
    def test_load_currencies(self):
        """
        Test case to load currencies
        """
        response = self.client.post(self.load_currencies_url, self.load_currencies_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Currency.objects.count(), 31)
        
    def get_currencies(self):
        """
        Test case to get all currencies
        """
        self.test_load_currencies()
        response = self.client.get(self.currency_url)
        # get items in response and check count
        self.assertEqual(len(response.data), 31)
    
    # def test_load_historical_data(self):
    #     """
    #     Test case to load historical data
    #     """
    #     self.load_currencies_data["load_historical_data"] = True
    #     # Pass data as query parameters
    #     response = self.client.post(self.load_currencies_url, self.load_currencies_data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(CurrencyConversionRates.objects.count() > 0, True)