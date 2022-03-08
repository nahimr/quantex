from xmlrpc.client import DateTime
from django.db import models
from django.contrib.postgres.fields import ArrayField
from numpy import float64

class MarketData(models.Model):

    date: DateTime = models.DateTimeField(primary_key=True)
    open: list  = ArrayField(base_field=models.FloatField())
    close: list = ArrayField(base_field=models.FloatField())
    low: list = ArrayField(base_field=models.FloatField())
    high: list = ArrayField(base_field=models.FloatField())
    volume: list = ArrayField(base_field=models.FloatField())
    dividends: list = ArrayField(base_field=models.FloatField())
    stocks_splits: list = ArrayField(base_field=models.FloatField())

    @classmethod
    def create(cls):
        marketData = cls()

        return marketData
