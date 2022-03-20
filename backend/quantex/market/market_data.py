import string
from django.db import models
from django.contrib.postgres.fields import ArrayField
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

    def setData(self, data : pd.DataFrame) -> None:
        if data is None:
            raise Exception("data is None !")

        self.date = pd.to_datetime(data.index, utc=True).tolist()
        self.close = data.get('Close').values.tolist()
        self.open = data.get('Open').values.tolist()
        self.low = data.get('Low').values.tolist()
        self.high = data.get('High').values.tolist()
        self.volume = data.get('Volume').values.tolist()

        dividends = data.get('Dividends').values.tolist()
        stocks_splits = data.get('Stock Splits').values.tolist()

        self.dividends = dividends if len(set(dividends)) > 1 else None
        self.stocks_splits = stocks_splits if len(set(stocks_splits)) > 1 else None
