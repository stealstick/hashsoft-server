from django.db import models

# Create your models here.

class Charger(models.Model):
    statId = models.CharField(max_length=100)
    statNm = models.CharField(max_length=100)
    chgerId = models.PositiveIntegerField(default=0)
    chgerType = models.PositiveIntegerField(default=0)
    stat = models.PositiveIntegerField(default=0)
    addrDoro = models.CharField(max_length=100)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    useTime = models.CharField(max_length=100)
    LastUsedTime = models.CharField(max_length=20)

    def __str__(self):
        return self.statNm