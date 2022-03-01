import string
from quantex.market.instrument import Instrument
from quantex.market.securities.index import Index

class ETF(Index):

    def __init__(self, symbol: string, instruments: 'list[Instrument]') -> None:
        super().__init__()

