import string
from quantex.market.instrument import Instrument

class Index(Instrument):

    instruments : 'list[Instrument]' = list()

    def __init__(self, symbol: string, instruments: 'list[Instrument]') -> None:
        super().__init__(symbol)
        self.instruments = instruments
