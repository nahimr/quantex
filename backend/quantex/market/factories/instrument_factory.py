import string
import yfinance as yf
from quantex.market.instrument import Instrument

class InstrumentFactory:

    def CreateInstrument(symbol : string) -> Instrument:
        # Fetch data from yfinance to create Instrument
        instrument = Instrument(symbol)
        ticker = yf.Ticker(instrument.symbol)
        hist = ticker.history(period="max")
        instrument.setData(hist)
        return instrument

    def CreateInstruments(symbols : list) -> 'list[Instrument]':
        instruments = list()

        tickers = yf.Tickers(' '.join(symbols))

        for symbol in symbols:
            ticker = tickers.tickers[symbol]
            hist = ticker.history(period="max")
            instrument = Instrument(ticker.ticker)
            instrument.setData(hist)
            instruments.append(instrument)

        return instruments

    def RefreshInstrument(instrument : Instrument) -> Instrument:
        instrument = InstrumentFactory.CreateInstrument(instrument.symbol)
        return instrument
