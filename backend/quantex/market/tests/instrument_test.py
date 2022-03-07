from django.test import TestCase
from quantex.market.factories.instrument_factory import InstrumentFactory
from utils.prints import *

class InstrumentTest(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_fetch_instrument(self) -> None:
        symbol = "AAPL"
        MsgDebug(f"Fetching {symbol} Stock")
        instr = InstrumentFactory.CreateInstrument(symbol)
        MsgSuccess(instr.getData())
