from pickle import NONE
import string
import pandas as pd

class Instrument(object):

    name : string = ""
    symbol : string = ""
    baseCurrency : string = ""
    region : string = ""
    data : pd.DataFrame

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
