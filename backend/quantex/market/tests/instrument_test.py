import pandas as pd
from django.test import TestCase
import yfinance
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

        ticker = yfinance.Ticker('GOOGL')
        MsgDebug(ticker.balance_sheet)
        MsgDebug(ticker.actions)
        MsgDebug(ticker.analysis)
        MsgDebug(ticker.calendar)
        MsgDebug(ticker.cashflow)
        MsgDebug(ticker.dividends)
        MsgDebug(ticker.earnings)
        MsgDebug(ticker.info)
        MsgDebug(ticker.major_holders)

        bs = pd.DataFrame.transpose(ticker.cashflow)
        bs.reset_index()
        MsgDebug(bs)