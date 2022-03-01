from curses.ascii import CR
import string
from utils.prints import MsgDebug
from quantex.market.securities.index import Index
from quantex.market.instrument import Instrument
import pandas as pd

class IndexFactory:

    def CreateIndex(symbol : string, instruments : 'list[Instrument]') -> Index:
        index = Index(symbol, instruments)
        # TODO: Trim data from when all instruments have data
        newData = list()

        for instrument in instruments:
            newData.append(instrument.data)

        data_concat = pd.concat(newData)

        by_row_index = data_concat.groupby(data_concat.index)
        data_means = by_row_index.mean()
        
        index.setData(data_means)

        return index

    def RefreshIndex(index : Index) -> Index:
        # TODO: For optimization append new data
        index = IndexFactory.CreateIndex(index.instruments)

        return index