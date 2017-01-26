from django.db import models

# Create your models here.

class Charger(models.Model):
    statId = models.CharField(max_length=100, help_text="충전소 아이디")
    statNm = models.CharField(max_length=100, help_text="충전소 이름")
    chgerId = models.PositiveIntegerField(default=0, help_text="충전기 아이디")
    chgerType = models.PositiveIntegerField(default=0, help_text="충전기 타입")
    stat = models.PositiveIntegerField(default=0, help_text="실시간 정보")
    addrDoro = models.CharField(max_length=100, help_text="도로명")
    lat = models.FloatField(default=0, help_text="위도")
    lng = models.FloatField(default=0, help_text="경도")
    useTime = models.CharField(max_length=100, help_text="사용 가능 시간")
    LastUsedTime = models.CharField(max_length=20, help_text="마지막 사용 시간")

    def __str__(self):
        return self.statNm