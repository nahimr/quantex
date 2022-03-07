import string
import pandas as pd
from django.db import models
from quantex.market.market_data import MarketData

class Instrument(models.Model):

    symbol : string = models.CharField(primary_key=True, max_length=5, unique=True)
    name : string = models.CharField(max_length=64)
    baseCurrency : string = models.CharField(max_length=3)
    region : string = models.CharField(max_length=128)
    data : MarketData = models.ForeignKey(MarketData, on_delete=models.CASCADE)

    def __init__(self, symbol : string) -> None:
        self.symbol = symbol
    
    def getName(self) -> string:
        return self.name

    def getSymbol(self) -> string:
        return self.symbol

    def getBaseCurrency(self) -> string:
        return self.baseCurrency
        
    def getRegion(self) -> string:
        return self.region

    def getClose(self) -> pd.DataFrame:
        return self.data.get("Close")
    
    def getOpen(self) -> pd.DataFrame:
        return self.data.get("Open")

    def getHigh(self) -> pd.DataFrame:
        return self.data.get("High")

    def getLow(self) -> pd.DataFrame:
        return self.data.get("Low")

    def setData(self, data : pd.DataFrame) -> None:
        self.data = data

    def getData(self) -> pd.DataFrame:
        return self.data
