import string
from django.db import IntegrityError, models, transaction
from django.db.models.query import QuerySet
import yfinance as yf
from quantex.financials.cashflow import CashFlow
from utils.prints import MsgDebug, MsgError, MsgSuccess
from quantex.market.market_data import MarketData

class InstrumentManager(models.Manager):

    def create_instruments(self, symbols: list):
        instruments = [self.create_instrument(symbol) for symbol in symbols]

        return instruments

    @transaction.atomic
    def update_instruments(self, symbols: list, full: bool = False):
        symbolsList = []
        symbolsString = ""

        try:
            instruments = self.filter(symbol__in=symbols)
            symbolsList = list(instruments.values_list("symbol", flat=True))
            symbolsString = ', '.join(symbolsList)

            MsgSuccess(f"{symbolsString} was fetched from database !")
        except IntegrityError as e:
            MsgError(e)

        if len(symbolsList) < 1:
            MsgError("No Instruments were fetched !")
            return

        MsgDebug(f"Getting {symbolsString} data from yFinance !")
        tickers = yf.Tickers(symbolsList)
        
        for instrument in instruments:
            MsgDebug(f"Getting {instrument.symbol} market data from yFinance !")
            ticker : yf.Ticker = tickers.tickers.get(instrument.symbol)

            if ticker is None: continue

            # Fetch what you need to update

            marketData : MarketData = instrument.data

            hist = ticker.history(
                period="max", 
                interval="1d",
                start=marketData.date[-1] # Fetch last date entry in db                
            )

            instrument.details = ticker.info
            instrument.data.setData(hist, append=True)

            if full:
                instrument.cashFlow.setData(ticker.cashflow, append=True)
                instrument.region = ticker.info.get('country')
                instrument.name = ticker.info.get('shortName')

            MsgDebug(f"Updating {instrument.name} instrument object to database !")

            try:
                instrument.data.save()
                if full: instrument.cashFlow.save()
                instrument.save()
            except IntegrityError as e:
                MsgError(e)

            MsgSuccess(f"Instrument {instrument.name} was updated with success !")

        return instruments

    @transaction.atomic
    def create_instrument(self, symbol: string):
        try:
            instrument, created = self.get_or_create(symbol=symbol)
            MsgDebug(f"{symbol} was created in database !" if created else f"{symbol} already created !")
            if not created:
                MsgSuccess(f"{symbol} was fetched with success from database !")
        except IntegrityError as e:
            MsgError(e)

        if not created: 
            MsgDebug(f"Updating {symbol} !")
        
        MsgDebug(f"Getting {symbol} data from yFinance !")
        ticker = yf.Ticker(instrument.symbol)
        MsgDebug(f"Getting {symbol} market data from yFinance !")

        historySettings : dict = {
            'period' : "max",
            'interval' : '1d',
        }

        if instrument.data is not None:
            historySettings['start'] = instrument.data.date[-1], # Fetch last date entry in db

        hist = ticker.history(**historySettings)

        if len(hist) < 1:
            instrument.delete()

            MsgError(f"{symbol} ticker doesn't exist !")
            raise Exception(f"{symbol} ticker doesn't exist !")

        instrument.data = MarketData(symbol=symbol)
        instrument.cashFlow = CashFlow(symbol=symbol)
        instrument.details = ticker.info
        instrument.region = ticker.info.get('country')
        instrument.name = ticker.info.get('shortName')
        instrument.data.setData(hist)
        instrument.cashFlow.setData(ticker.cashflow)

        MsgDebug(f"Updating {instrument.name} instrument object to database !")

        try:
            instrument.data.save()
            instrument.cashFlow.save()
            instrument.save()
        except IntegrityError as e:
            MsgError(e)

        MsgSuccess(f"Instrument {instrument.name} was updated with success !")

        return instrument

    def get_instruments(self, symbols : list) -> QuerySet:
        if symbols is None:
            raise Exception("Symbols list is empty !")

        instruments = []

        try:
            instruments = self.filter(symbol__in=symbols)
        except IntegrityError as e:
            MsgError(e)

        return instruments
