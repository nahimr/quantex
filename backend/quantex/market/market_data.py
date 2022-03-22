import string
from django.db import models
from django.contrib.postgres.fields import ArrayField
import pandas as pd
from utils.prints import MsgDebug

class MarketData(models.Model):

    symbol: string = models.CharField(primary_key=True, max_length=7, unique=True, null=False, default="")
    date: list = ArrayField(base_field=models.DateTimeField())
    open: list  = ArrayField(base_field=models.FloatField())
    close: list = ArrayField(base_field=models.FloatField())
    low: list = ArrayField(base_field=models.FloatField())
    high: list = ArrayField(base_field=models.FloatField())
    volume: list = ArrayField(base_field=models.FloatField(null=True))
    dividends: list = ArrayField(base_field=models.FloatField(null=True), null=True)
    stocks_splits: list = ArrayField(base_field=models.FloatField(null=True), null=True)

    __attrs = [
        ('Close', 'close'),
        ('Open', 'open'),
        ('Low', 'low'),
        ('High', 'high'),
        ('Volume', 'volume'),
    ]

    @classmethod
    def create(cls):
        marketData = cls()

        return marketData

    def getData(self) -> pd.DataFrame:
        dataFrame = pd.DataFrame({
            'Date': self.date,
            'Close': self.close,
            'Open': self.open,
            'Low': self.low,
            'High': self.close,
            'Volume': self.volume,
            'Dividends': self.dividends,
            'Stock Splits': self.stocks_splits,
        })
        dataFrame.set_index('Date')   

        return dataFrame

    def setData(self, data : pd.DataFrame, append : bool = False) -> None:
        if data is None:
            raise Exception("data is None !")
        
        for attr in self.__attrs:
            nameInDF = attr[0]
            attributeInObject = attr[1]
            value = data.get(nameInDF)
            if value is None: continue

            if append:
                listToExtend : list = getattr(self, attributeInObject)
                listToExtend.extend(value.values.tolist())
                setattr(self, attributeInObject, listToExtend)
                continue

            setattr(self, attributeInObject, value.values.tolist())     

        date_list = pd.to_datetime(data.index, utc=True).tolist()

        dividends = data.get('Dividends').values.tolist()
        stocks_splits = data.get('Stock Splits').values.tolist()

        if append:
            if self.dividends is not None:
                self.dividends.extend(dividends)

            if self.stocks_splits is not None:
                self.stocks_splits.extend(stocks_splits)
            
            self.date.extend(date_list)
            return

        self.date = date_list
        self.dividends = dividends if len(set(dividends)) > 1 else None
        self.stocks_splits = stocks_splits if len(set(stocks_splits)) > 1 else None
