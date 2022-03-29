from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from quantex.market.market_data import MarketData
from quantex.market.instrument import Instrument
from quantex.serializers import InstrumentSerializer, MarketDataSerializer
from rest_framework import permissions

class Instruments(APIView):

    def get(self, request: Request, format = None):
        instruments = Instrument.objects.all()
        serializer = InstrumentSerializer(instruments)
        return Response(serializer.data)

class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [permissions.IsAuthenticated]

class MarketDataViewSet(viewsets.ModelViewSet):
    queryset = MarketData.objects.all()
    serializer_class = MarketDataSerializer
    permission_classes = [permissions.IsAuthenticated]
