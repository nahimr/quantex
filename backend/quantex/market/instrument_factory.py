import string
from backend.quantex.market.instrument import Instrument

class InstrumentFactory:

    def CreateInstrument(symbol : string) -> Instrument:
        # Fetch symbol to create Instrument
        instrument = Instrument(symbol)

        return instrument
