from pickle import NONE
import string

class Instrument:

    symbol : string = ""
    baseCurrency : string = ""
    region : string = ""
    ask : float = 0.0
    bid : float = 0.0
    name : string = ""

    def __init__(self, symbol : string) -> None:
        self.symbol = symbol

    def setBaseCurrency(self, baseCurrency : string) -> None:
        self.baseCurrency = baseCurrency

    def setRegion(self, region : string) -> None:
        self.region = region
    
    def setAsk(self, ask : float) -> None:
        self.ask = ask

    def setBid(self, bid : float) -> None:
        self.bid = bid
    
    def setName(self, name : string):
        self.name = name
    