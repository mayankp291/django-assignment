from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Currency
from .serializers import CurrencySerializer
from rest_framework.parsers import JSONParser
from utils.utils import fetch_and_store_currencies, populate_exchange_rates
from django.db.models import Q


class CurrencyListApiView(APIView):
    """
    API View to list all currencies
    """

    def get(self, request):
        try:
            query = request.query_params.get("filter")
            # filtering currencies based on query
            if query is not None:
                currencies = Currency.objects.filter(
                    Q(name__icontains=query) | Q(symbol__icontains=query)
                ).order_by("name")
            else:
                currencies = Currency.objects.all().order_by("name")
            serializer = CurrencySerializer(currencies, many=True)

            # format data to Name (Symbol) format
            output = []
            for currency in serializer.data:
                output.append(f"{currency['name']} ({currency['symbol']})")

            return Response(
                {
                    "status": "success",
                    "message": "Currencies fetched successfully",
                    "data": output,
                    "count": len(output),
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": "Failed to fetch currencies",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def post(self, request):
        """
        API View to add a new currency
        """
        data = JSONParser().parse(request)
        serializer = CurrencySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "message": "Currency created successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "status": "error",
                    "message": "Currency creation failed",
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class LoadCurrencies(APIView):
    """
    API View to initialise the database. Gets the latest currencies (and/or historical data) from the API and stores it in the database
    """
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            historical_from_date = data.get("historical_from_date")
            historical_to_date = data.get("historical_to_date")
            load_historical_data = data.get("load_historical_data")
            fetch_and_store_currencies()

            if load_historical_data:
                populate_exchange_rates(historical_from_date, historical_to_date)

            return Response(
                {"status": "success", "message": "Currencies loaded successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "status": "error",
                    "message": "Failed to load currencies",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
