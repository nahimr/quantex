import string
from quantex.market.securities.etf import ETF

class ETFFactory:

    def CreateETF(symbol : string, instruments : 'list[ETF]') -> ETF:
        etf = ETF(symbol, instruments)
        # TODO : Make sums of each instruments
        return etf
