from rest_framework import viewsets
from quantex.market.instrument import Instrument
from quantex.serializers import InstrumentSerializer
# Create your views here.

class InstrumentListCreate(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    

