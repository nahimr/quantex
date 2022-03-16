from xmlrpc.client import Boolean
from django.db import models
from numpy import float64, integer

class Sustainability(models.Model):

    # TODO: Make it arrayble !
    palmOil : Boolean = models.BooleanField(null=True)
    controversialWeapons : Boolean = models.BooleanField(null=True)
    gambling : Boolean = models.BooleanField(null=True)
    socialScore : float64 = models.FloatField(null=True)
    nuclear : Boolean = models.BooleanField(null=True)
    furLeather : Boolean = models.BooleanField(null=True)
    alcoholic : Boolean = models.BooleanField(null=True)
    gmo : Boolean = models.BooleanField(null=True)
    socialPercentile : float64 = models.FloatField(null=True)
    peerCount : integer = models.IntegerField(null=True)
    governanceScore : float64 = models.FloatField(null=True)
    environmentPercentile : float64 = models.FloatField(null=True)
    animalTesting : Boolean = models.BooleanField(null=True)
    tobacco : Boolean = models.BooleanField(null=True)
    totalEsg : float64 = models.FloatField(null=True)
    highestControversy : integer = models.IntegerField(null=True)
    esgPerformance : integer = models.IntegerField(null=True)
    coal : Boolean = models.BooleanField(null=True)
    pesticides : Boolean = models.BooleanField(null=True)
    adult : Boolean = models.BooleanField(null=True)
    smallArm : Boolean = models.BooleanField(null=True)
    militaryContract : Boolean = models.BooleanField(null=True)
    percentile : float64 = models.FloatField(null=True)
    governancePercentile : float64 = models.FloatField(null=True)
