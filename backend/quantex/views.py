from rest_framework import viewsets
from quantex.market.instrument import Instrument
from quantex.serializers import InstrumentSerializer
from rest_framework import permissions
# Create your views here.

class InstrumentViewSet(viewsets.ModelViewSet):
    queryset = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    permission_classes = [permissions.IsAuthenticated]
