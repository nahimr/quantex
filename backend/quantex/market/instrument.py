import string
import pandas as pd
from django.db import models
from quantex.financials.cashflow import CashFlow
from quantex.market.managers.InstrumentManager import InstrumentManager
from quantex.market.market_data import MarketData
from utils.prints import *

class Instrument(models.Model):

    symbol : string = models.CharField(primary_key=True, max_length=5, unique=True, null=False)
    name : string = models.CharField(max_length=64)
    baseCurrency : string = models.CharField(max_length=3)
    region : string = models.CharField(max_length=3)
    data : MarketData = models.ForeignKey(MarketData, related_name='quantex_marketdata', null=True, on_delete=models.CASCADE)
    cashFlow : CashFlow = models.ForeignKey(CashFlow, related_name='quantex_cashflow', null=True, on_delete=models.CASCADE)
    objects = InstrumentManager()
    
    def getName(self) -> string:
        return self.name

    def getSymbol(self) -> string:
        return self.symbol

    def getBaseCurrency(self) -> string:
        return self.baseCurrency
        
    def getRegion(self) -> string:
        return self.region

    def getClose(self) -> list:
        return self.data.close
    
    def getOpen(self) -> list:
        return self.data.open

    def getHigh(self) -> list:
        return self.data.high

    def getLow(self) -> list:
        return self.data.low

    def setName(self, name : string) -> None:
        self.name = name

    def setData(self, data : pd.DataFrame) -> None:
        if data is None:
            raise Exception("data is None !")

        self.data.date = pd.to_datetime(data.index, utc=True).tolist()
        self.data.close = data.get('Close').values.tolist()
        self.data.open = data.get('Open').values.tolist()
        self.data.low = data.get('Low').values.tolist()
        self.data.high = data.get('High').values.tolist()
        self.data.volume = data.get('Volume').values.tolist()

        dividends = data.get('Dividends').values.tolist()
        stocks_splits = data.get('Stock Splits').values.tolist()

        self.data.dividends = dividends if len(set(dividends)) > 1 else None
        self.data.stocks_splits = stocks_splits if len(set(stocks_splits)) > 1 else None

    def setCashFlow(self, cf : pd.DataFrame) -> None:
        if cf is None:
            raise Exception("Cash Flow data is None !")
        
        data = pd.DataFrame.transpose(cf)

        attrs = [
            ("Investments", "investments"),
            ("Change To Liabilities", "changeToLiabilities"),
            ("Total Cashflows From Investing Activities", "totCFInvestingActivities"),
            ("Net Borrowings", "netBorrowings"),
            ("Total Cash From Financing Activities", "totCFinancingActivities"),
            ("Change To Operating Activities", "changeToOperatingActivities"),
            ("Net Income", "netIncome"),
            ("Change In Cash", "changeInCash"),
            ("Repurchase Of Stock", "repurchaseOfStock"),
            ("Effect Of Exchange Rate", "effectOfExchangeRate"),
            ("Total Cash From Operating Activities", "totCFOperatingActivites"),
            ("Depreciation", "depreciation"),
            ("Other Cashflows From Investing Activities", "otherCFInvestingActivites"),
            ("Change To Account Receivables", "changeToAccountReceivables"),
            ("Other Cashflows From Financing Activities", "otherCFFinancingActivites"),
            ("Change To Netincome", "changeToNetIncome"),
            ("Capital Expenditures", "capitalExpenditures"),
        ]

        for attr in attrs:
            nameInDF = attr[0]
            attributeInObject = attr[1]
            value = data.get(nameInDF)
            
            MsgDebug(f"{value}")
            if value is None: continue
            setattr(self.cashFlow, attributeInObject, value.values.tolist())

    def __str__(self) -> str:
        return f"Symbol: {self.symbol},\nName: {self.name},\nBase Currency: {self.baseCurrency},\nRegion: {self.region}"
