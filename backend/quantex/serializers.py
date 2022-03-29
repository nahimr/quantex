from rest_framework import serializers
from quantex.market.market_data import MarketData
from quantex.market.instrument import Instrument

class MarketDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketData
        fields = ('symbol', 'date', 'open', 'close', 'low', 'high', 'volume', 'dividends', 'stocks_splits')


class InstrumentSerializer(serializers.ModelSerializer):
    # data = MarketDataSerializer(many=False, read_only=True)
    
    class Meta:
        model = Instrument
        fields = ('name', 'symbol', 'region', 'data', 'cashFlow', 'details')
