import os
import time

from django.db import models


def get_upload_path_01(instance, filename):
    currently = time.strftime("%y%m%d%H%M%S")
    return os.path.join(
      "chargers" , "{}_{}.jpg".format(currently, instance.sid + "_01")
    )

def get_upload_path_02(instance, filename):
    currently = time.strftime("%y%m%d%H%M%S")
    return os.path.join(
      "chargers" , "{}_{}.jpg".format(currently, instance.sid + "_02")
    )


class Charger(models.Model):
    unique_id = models.CharField(max_length=100, help_text="충전소 고유 아이디", unique=True)
    sid = models.CharField(max_length=100, help_text="충전소 아이디")
    name = models.CharField(max_length=100, help_text="충전소 이름")
    cid = models.CharField(max_length=100, default=0, help_text="충전기 아이디")
    ctype = models.PositiveIntegerField(default=0, help_text="충전기 타입")
    stat = models.PositiveIntegerField(default=0, help_text="실시간 정보")
    addrDoro = models.CharField(max_length=100, help_text="도로명")
    lat = models.CharField(max_length=100, default=0, help_text="위도")
    lng = models.CharField(max_length=100, default=0, help_text="경도")
    pay = models.CharField(max_length=100, default="", blank=True, help_text="가격")
    tel = models.CharField(max_length=100, default="", help_text="전화번호", blank=True)
    useTime = models.CharField(max_length=100, default=0, help_text="사용 가능 시간")
    LastUsedTime = models.CharField(max_length=20, help_text="마지막 사용 시간")
    bid=models.CharField(max_length=20, default="etc", blank=False)
    charger_img1= models.ImageField(upload_to=get_upload_path_01, default="defalutChargerImg.jpg")
    charger_img2= models.ImageField(upload_to=get_upload_path_02, default="defalutChargerImg.jpg")

    def __str__(self):
        return self.name



