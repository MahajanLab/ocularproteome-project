from django.db import models


class Protein(models.Model):
    pID = models.CharField
    pName = models.CharField
    pFoveaAvg = models.IntegerField
    pMaculaAvg = models.IntegerField
    pPeripheryAvg = models.IntegerField
