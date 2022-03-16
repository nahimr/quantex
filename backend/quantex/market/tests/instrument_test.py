from django.test import TestCase
import yfinance
from quantex.market.instrument import Instrument
from quantex.market.factories.instrument_factory import InstrumentFactory
from utils.prints import *

class InstrumentTest(TestCase):

    def setUp(self) -> None:
        pass

    def test_fetch_instrument(self) -> None:
        # instrument : Instrument = Instrument(symbol="AAPL", name="Apple", baseCurrency="USD", region="USA")
        # instrument.save()
        # MsgSuccess(Instrument.objects.values_list('symbol', flat=True))
        # instrument2 : Instrument = Instrument.objects.get(pk='APPL')
        # #MsgDebug(f"Fetching {self.instrument.symbol} Stock")
        # #instr = InstrumentFactory.CreateInstrument(instrument.symbol)
        # #MsgSuccess(self.instrument.getData())

        ticker = yfinance.Ticker('AAPL')
        MsgDebug(ticker.balance_sheet)
        MsgDebug(ticker.actions)
        MsgDebug(ticker.analysis)
        MsgDebug(ticker.calendar)
        MsgDebug(ticker.cashflow)
        MsgDebug(ticker.dividends)
        MsgDebug(ticker.earnings)
        MsgDebug(ticker.info)
        MsgDebug(ticker.major_holders)
        MsgDebug(ticker.sustainability)
