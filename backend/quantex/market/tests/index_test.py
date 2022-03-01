from django.test import TestCase
from quantex.market.factories.instrument_factory import InstrumentFactory
from quantex.market.factories.index_factory import IndexFactory
from utils.prints import *

class IndexTest(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test_fetch_index(self) -> None:
        symbol = "GAFAMIndex"
        symbolsToFetch = ["AAPL", "MSFT", "GOOGL", "AMZN", "FB"]
        MsgDebug("Fetching AAPL, MSFT Stock")
        index = IndexFactory.CreateIndex(symbol, InstrumentFactory.CreateInstruments(symbolsToFetch))
        MsgSuccess(f"{symbol} made with success !")
        MsgDebug(index.getData())
