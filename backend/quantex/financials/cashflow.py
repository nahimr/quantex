import string
from django.db import models
from django.contrib.postgres.fields import ArrayField

class CashFlow(models.Model):

    symbol : string = models.CharField(primary_key=True, max_length=5, unique=True, null=False, default="")
    investments : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    changeToLiabilities : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    totCFInvestingActivities : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    netBorrowings : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    totCFinancingActivities : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    changeToOperatingActivities : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    netIncome : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    changeInCash : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    repurchaseOfStock : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    effectOfExchangeRate : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    totCFOperatingActivites : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    depreciation : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    otherCFInvestingActivites : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    changeToAccountReceivables : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    otherCFFinancingActivites : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    changeToNetIncome : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
    capitalExpenditures : list = ArrayField(base_field=models.IntegerField(null=True), null=True)
