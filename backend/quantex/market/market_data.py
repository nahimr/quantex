from enum import unique
import string
from django.db import models
from django.contrib.postgres.fields import ArrayField
from numpy import float64

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
