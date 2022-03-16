import string
from django.db import models
import yfinance as yf
from quantex.market.market_data import MarketData
from utils.prints import MsgDebug

class InstrumentManager(models.Manager):

    def create_instrument(self, symbol: string, name: string, baseCurrency: string, region: string):
        # TODO: Implement Try Except
        instrument, created = self.get_or_create(symbol=symbol, name=name, baseCurrency=baseCurrency, region=region)

        ticker = yf.Ticker(instrument.symbol)
        hist = ticker.history(period="max", interval="1d")
        instrument.data = MarketData(symbol=symbol)
        instrument.setData(hist)
        instrument.data.save()
        instrument.save()
        return instrument

