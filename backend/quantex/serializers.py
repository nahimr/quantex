from rest_framework import serializers
from quantex.market.instrument import Instrument

class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = ('name', 'symbol', 'baseCurrency', 'region', 'data')
