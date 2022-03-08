from django.test import TestCase
from quantex.market.instrument import Instrument
from quantex.market.factories.instrument_factory import InstrumentFactory
from utils.prints import *

class InstrumentTest(TestCase):

    def setUp(self) -> None:
        Instrument.objects.create(symbol="AAPL", name="Apple")

    def test_fetch_instrument(self) -> None:
        instrument : Instrument = Instrument.objects.get(symbol="APPL")
        MsgDebug(f"Fetching {instrument.symbol} Stock")
        #instr = InstrumentFactory.CreateInstrument(instrument.symbol)
        MsgSuccess(instrument.getData())
