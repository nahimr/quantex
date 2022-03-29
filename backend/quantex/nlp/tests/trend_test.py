from django.test import TestCase
from pytrends.request import TrendReq
from utils.prints import *
from quantex.market.instrument import Instrument

class TrendTest(TestCase):
    instruments : list
    testSymbols : list = ['GOOGL', 'AAPL']

    def setUp(self) -> None:
        # Fill the database with Instruments
        self.instruments = Instrument.objects.create_instruments(self.testSymbols)

    def test_trend(self):
        # Perform trending request
        trend = TrendReq(hl='en-US', tz=0)

        # Keywords list
        kw_list = []

        # Fill Keywords list with instruments names
        for instrument in self.instruments:
            kw_list.append(instrument.name)

        trend.build_payload(kw_list, cat=0, timeframe='today 12-m') 

        interests = trend.interest_by_region(resolution='France', inc_low_vol=True, inc_geo_code=False)
