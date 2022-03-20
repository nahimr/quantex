import string
from django.db import IntegrityError, models
import yfinance as yf
from quantex.financials.cashflow import CashFlow
from utils.prints import MsgDebug, MsgError, MsgSuccess
from quantex.market.market_data import MarketData

class InstrumentManager(models.Manager):

    def create_instrument(self, symbol: string, name: string, baseCurrency: string, region: string):
        try:
            instrument, created = self.get_or_create(symbol=symbol, name=name, baseCurrency=baseCurrency, region=region)
            MsgDebug(f"{symbol} was created in database !" if created else f"{symbol} already created !")
            if not created:
                MsgSuccess(f"{symbol} was fetched with success from database !")
        except IntegrityError as e:
            MsgError(e)

        if not created: 
            MsgDebug(f"Updating {symbol} !")
        
        MsgDebug(f"Getting {symbol} data from yFinance !")
        ticker = yf.Ticker(instrument.symbol)
        MsgDebug(f"Getting {symbol} history from yFinance !")
        hist = ticker.history(period="max", interval="1d")
        instrument.data = MarketData(symbol=symbol)
        instrument.cashFlow = CashFlow(symbol=symbol)
        
        instrument.data.setData(hist)
        instrument.cashFlow.setData(ticker.cashflow)

        MsgDebug(f"Updating {name} instrument object to database !")

        try:
            instrument.data.save()
            instrument.cashFlow.save()
            instrument.save()
        except IntegrityError as e:
            MsgError(e)

        MsgSuccess(f"Instrument {name} was updated with success !")
        return instrument
