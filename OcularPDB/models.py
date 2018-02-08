from django.db import models

# Create your models here.


class Protein(models.Model):
    pID = models.CharField
    pName = models.CharField
    pFoveaAvg = models.IntegerField
    pMaculaAvg = models.IntegerField
    pPeripheryAvg = models.IntegerField

