from enum import unique
import string
from django.db import models
from django.contrib.postgres.fields import ArrayField
from numpy import float64
import pandas as pd

class MarketData(models.Model):

    symbol: string = models.CharField(primary_key=True, max_length=5, unique=True, null=False, default="")
    date: list = ArrayField(base_field=models.DateTimeField())
    open: list  = ArrayField(base_field=models.FloatField())
    close: list = ArrayField(base_field=models.FloatField())
    low: list = ArrayField(base_field=models.FloatField())
    high: list = ArrayField(base_field=models.FloatField())
    volume: list = ArrayField(base_field=models.FloatField(null=True))
    dividends: list = ArrayField(base_field=models.FloatField(null=True), null=True)
    stocks_splits: list = ArrayField(base_field=models.FloatField(null=True), null=True)

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
