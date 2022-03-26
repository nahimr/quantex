import string
from django.db import models
from quantex.financials.cashflow import CashFlow
from quantex.market.managers.InstrumentManager import InstrumentManager
from quantex.market.market_data import MarketData
from utils.prints import *

class Instrument(models.Model):

    symbol : string = models.CharField(primary_key=True, max_length=7, unique=True, null=False)
    name : string = models.CharField(max_length=64)
    region : string = models.CharField(max_length=56)
    data : MarketData = models.ForeignKey(MarketData, related_name='quantex_marketdata', null=True, on_delete=models.CASCADE)
    cashFlow : CashFlow = models.ForeignKey(CashFlow, related_name='quantex_cashflow', null=True, on_delete=models.CASCADE)
    details : string = models.JSONField(null=True)
    objects = InstrumentManager()
    
    def getName(self) -> string:
        return self.name

    def getSymbol(self) -> string:
        return self.symbol
        
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

    def __str__(self) -> str:
        return f"Symbol: {self.symbol},\nName: {self.name},\nRegion: {self.region}"
