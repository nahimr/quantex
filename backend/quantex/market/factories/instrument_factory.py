import string
import yfinance as yf
from quantex.market.instrument import Instrument

class InstrumentFactory:

    def CreateInstrument(symbol : string) -> Instrument:
        # Fetch symbol to create Instrument
        instrument = Instrument(symbol)
        ticker = yf.Ticker(instrument.symbol)
        hist = ticker.history(period="max")
        instrument.setData(hist)
        return instrument
