import string
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Sustainability(models.Model):

    symbol: string = models.CharField(primary_key=True, max_length=5, unique=True, null=False, default="")
    date: list = ArrayField(base_field=models.DateTimeField(null=True))
    palmOil : list = ArrayField(base_field=models.BooleanField(null=True))
    controversialWeapons : list = ArrayField(base_field=models.BooleanField(null=True))
    gambling : list = ArrayField(base_field=models.BooleanField(null=True))
    socialScore : list = ArrayField(base_field=models.FloatField(null=True))
    nuclear : list = ArrayField(base_field=models.BooleanField(null=True))
    furLeather : list = ArrayField(base_field=models.BooleanField(null=True))
    alcoholic : list = ArrayField(base_field=models.BooleanField(null=True))
    gmo : list = ArrayField(base_field=models.BooleanField(null=True))
    socialPercentile : list = ArrayField(base_field=models.FloatField(null=True))
    peerCount : list = ArrayField(base_field=models.IntegerField(null=True))
    governanceScore : list = ArrayField(base_field=models.FloatField(null=True))
    environmentPercentile : list = ArrayField(base_field=models.FloatField(null=True))
    animalTesting : list = ArrayField(base_field=models.BooleanField(null=True))
    tobacco : list = ArrayField(base_field=models.BooleanField(null=True))
    totalEsg : list = ArrayField(base_field=models.FloatField(null=True))
    highestControversy : list = ArrayField(base_field=models.IntegerField(null=True))
    esgPerformance : list = ArrayField(base_field=models.IntegerField(null=True))
    coal : list = ArrayField(base_field=models.BooleanField(null=True))
    pesticides : list = ArrayField(base_field=models.BooleanField(null=True))
    adult : list = ArrayField(base_field=models.BooleanField(null=True))
    smallArm : list = ArrayField(base_field=models.BooleanField(null=True))
    militaryContract : list = ArrayField(base_field=models.BooleanField(null=True))
    percentile : list = ArrayField(base_field=models.FloatField(null=True))
    governancePercentile : list = ArrayField(base_field=models.FloatField(null=True))

    @classmethod
    def create(cls):
        sus = cls()

        return sus
    