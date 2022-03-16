import string
import pandas as pd
from django.db import models
from quantex.financials.sustainability import Sustainability
from quantex.market.managers.InstrumentManager import InstrumentManager
from quantex.market.market_data import MarketData
from utils.prints import *

class Instrument(models.Model):

    symbol : string = models.CharField(primary_key=True, max_length=5, unique=True, null=False)
    name : string = models.CharField(max_length=64)
    baseCurrency : string = models.CharField(max_length=3)
    region : string = models.CharField(max_length=3)
    data : MarketData = models.ForeignKey(MarketData, related_name='quantex_marketdata', null=True, on_delete=models.CASCADE)
    sustainability : Sustainability = models.ForeignKey(Sustainability, related_name='quantex_sustainability', null=True, on_delete=models.CASCADE)
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

    def setSustainability(self, esg : pd.DataFrame) -> None:
        data = pd.DataFrame.transpose(esg)
        MsgDebug(data)
        # TODO: Refactoring with foreach
        #self.sustainability.date = pd.to_datetime(data.index, utc=True).tolist()
        self.sustainability.palmOil = data.get('palmOil').values.tolist()
        self.sustainability.controversialWeapons = data.get('controversialWeapons').values.tolist()
        self.sustainability.gambling = data.get('gambling').values.tolist()
        self.sustainability.socialScore = data.get('socialScore').values.tolist()
        self.sustainability.nuclear = data.get('nuclear').values.tolist()
        self.sustainability.furLeather = data.get('furLeather').values.tolist()
        self.sustainability.alcoholic = data.get('alcoholic').values.tolist()
        self.sustainability.gmo = data.get('gmo').values.tolist()
        self.sustainability.socialPercentile = data.get('socialPercentile').values.tolist()
        self.sustainability.peerCount = data.get('peerCount').values.tolist()
        self.sustainability.governanceScore = data.get('governanceScore').values.tolist()
        self.sustainability.environmentPercentile = data.get('environmentPercentile').values.tolist()
        self.sustainability.animalTesting = data.get('animalTesting').values.tolist()
        self.sustainability.tobacco = data.get('tobacco').values.tolist()
        self.sustainability.totalEsg = data.get('totalEsg').values.tolist()
        self.sustainability.highestControversy = data.get('highestControversy').values.tolist()
        self.sustainability.esgPerformance = data.get('esgPerformance').values.tolist()
        self.sustainability.coal = data.get('coal').values.tolist()
        self.sustainability.pesticides = data.get('pesticides').values.tolist()
        self.sustainability.adult = data.get('adult').values.tolist()
        self.sustainability.smallArm = data.get('smallArm')
        self.sustainability.militaryContract = data.get('militaryContract').values.tolist()
        self.sustainability.percentile = data.get('percentile').values.tolist()
        self.sustainability.governancePercentile = data.get('governancePercentile').values.tolist()


    def __str__(self) -> str:
        return f"Symbol: {self.symbol},\nName: {self.name},\nBase Currency: {self.baseCurrency},\nRegion: {self.region}"
