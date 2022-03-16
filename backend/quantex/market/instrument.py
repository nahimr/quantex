import string
import pandas as pd
from django.db import models
from quantex.market.managers.InstrumentManager import InstrumentManager
from quantex.market.market_data import MarketData

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
        self.data.dividends = data.get('Dividends').values.tolist()
        self.data.stocks_splits = data.get('Stock Splits').values.tolist()

    def getData(self) -> pd.DataFrame:
        dataFrame = pd.DataFrame({
            'Date': self.data.date,
            'Close': self.data.close,
            'Open': self.data.open,
            'Low': self.data.low,
            'High': self.data.close,
            'Volume': self.data.volume,
            'Dividends': self.data.dividends,
            'Stock Splits': self.data.stocks_splits,
        })
        dataFrame.set_index('Date')   

        return dataFrame

    def __str__(self) -> str:
        return f"Symbol: {self.symbol},\nName: {self.name},\nBase Currency: {self.baseCurrency},\nRegion: {self.region}"
