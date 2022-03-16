import string
import pandas as pd
import pytz
import yfinance as yf
from django.db import models
from utils.prints import MsgDebug
from quantex.market.managers.InstrumentManager import InstrumentManager
from quantex.market.market_data import MarketData
import numpy as np

class Instrument(models.Model):

    symbol : string = models.CharField(primary_key=True, max_length=5, unique=True, null=False)
    name : string = models.CharField(max_length=64)
    baseCurrency : string = models.CharField(max_length=3)
    region : string = models.CharField(max_length=3)
    data : MarketData = models.ForeignKey(MarketData, related_name='quantex_marketdata', null=True, on_delete=models.CASCADE)
    objects = InstrumentManager()
    
    def getName(self) -> string:
        return self.name

    def getSymbol(self) -> string:
        return self.symbol

    def getBaseCurrency(self) -> string:
        return self.baseCurrency
        
    def getRegion(self) -> string:
        return self.region

    def getClose(self) -> list:
        return self.data.close
    
    def getOpen(self) -> list:
        return self.data.open

    def getHigh(self) -> list:
        return self.data.high

    def getLow(self) -> list:
        return self.data.low

    def setName(self, name : string) -> None:
        self.name = name

    def setData(self, data : pd.DataFrame) -> None:
        self.data.date = pd.to_datetime(data.index, utc=True).tolist()
        self.data.close = data.get('Close').values.tolist()
        self.data.open = data.get('Open').values.tolist()
        self.data.low = data.get('Low').values.tolist()
        self.data.high = data.get('High').values.tolist()
        self.data.volume = data.get('Volume').values.tolist()

    def getData(self) -> pd.DataFrame:
        dataFrame = pd.DataFrame()

        dataFrame.insert(loc=0, column='Date', value=self.data.date)
        dataFrame.insert(loc=0, column='Close', value=self.data.close)
        dataFrame.insert(loc=0, column='Open', value=self.data.open)
        dataFrame.insert(loc=0, column='Low', value=self.data.low)
        dataFrame.insert(loc=0, column='High', value=self.data.high)
        dataFrame.insert(loc=0, column='Volume', value=self.data.volume)
        dataFrame.insert(loc=0, column='Dividends', value=self.data.dividends)
        dataFrame.insert(loc=0, column='Stock Splits', value=self.data.stocks_splits)

        return dataFrame
