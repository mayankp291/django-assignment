from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Currency
from .serializers import CurrencySerializer
from rest_framework.parsers import JSONParser
from utils.utils import fetch_and_store_currencies, populate_exchange_rates


class CurrencyListApiView(APIView):
    """
    API View to list all currencies
    """
    parser_classes = [JSONParser]
    def get(self, request):
        try:
            currencies = Currency.objects.all()
            serializer = CurrencySerializer(currencies, many=True)
            return Response({
                "status": "success",
                "message": "Currencies fetched successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "message": "Failed to fetch currencies",
                "errors": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        """
        API View to add a new currency
        """	
        data = {
            "name": request.data.get("name"),
            "symbol": request.data.get("symbol")
        }
        serializer = CurrencySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Currency created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": "error",
                "message": "Currency creation failed",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

class LoadCurrencies(APIView):
    def get(self, request):
        try:
            fetch_and_store_currencies()
            populate_exchange_rates()
            return Response({
                "status": "success",
                "message": "Currencies loaded successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "message": "Failed to load currencies",
                "errors": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            