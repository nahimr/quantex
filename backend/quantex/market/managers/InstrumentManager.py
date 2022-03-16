import string
from django.db import models
import yfinance as yf
from quantex.financials.sustainability import Sustainability
from quantex.market.market_data import MarketData

class InstrumentManager(models.Manager):

    def create_instrument(self, symbol: string, name: string, baseCurrency: string, region: string):
        # TODO: Implement Try Except
        instrument, created = self.get_or_create(symbol=symbol, name=name, baseCurrency=baseCurrency, region=region)
        
        ticker = yf.Ticker(instrument.symbol)
        hist = ticker.history(period="max", interval="1d")
        instrument.data = MarketData(symbol=symbol)
        instrument.sustainability = Sustainability(symbol=symbol)
        # instrument.setData(hist)
        # instrument.setSustainability(ticker.sustainability)
        instrument.data.save()
        instrument.sustainability.save()
        instrument.save()
        return instrument
