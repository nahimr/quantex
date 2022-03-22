import string
from django.db import models
from django.contrib.postgres.fields import ArrayField
import pandas as pd

class CashFlow(models.Model):

    symbol : string = models.CharField(primary_key=True, max_length=7, unique=True, null=False, default="")
    date : list = ArrayField(base_field=models.DateTimeField(null=True))
    investments : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    changeToLiabilities : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    totCFInvestingActivities : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    netBorrowings : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    totCFinancingActivities : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    changeToOperatingActivities : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    netIncome : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    changeInCash : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    repurchaseOfStock : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    effectOfExchangeRate : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    totCFOperatingActivites : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    depreciation : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    otherCFInvestingActivites : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    changeToAccountReceivables : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    otherCFFinancingActivites : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    changeToNetIncome : list = ArrayField(base_field=models.FloatField(null=True), null=True)
    capitalExpenditures : list = ArrayField(base_field=models.FloatField(null=True), null=True)

    __attrs : list = [
            ("Date", "date"),
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

    def getData(self) -> pd.DataFrame:
        dataFrame = pd.DataFrame()

        for attr in self.__attrs:
            nameInDF = attr[0]
            attributeInObject = attr[1]
            value = getattr(self, attributeInObject)
            if value is None: continue
            dataFrame.insert(0, nameInDF, value)

        dataFrame.reset_index()
        dataFrame.set_index('Date')   

        return dataFrame

    def setData(self, cf : pd.DataFrame, append : bool = False) -> None:
        if cf is None:
            raise Exception("Cash Flow data is None !")
        
        data = pd.DataFrame.transpose(cf)

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

        if data.index is None: return

        date_list = pd.to_datetime(data.index, utc=True).tolist()

        if append:
            self.date.extend(date_list)
            return

        self.date = date_list
