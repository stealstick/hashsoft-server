from django.test import TestCase

from .models import Charger


class ChargersTestCase(TestCase):
    def setUp(self):
        self.charger1 = Charger.objects.create(
            statId=11110003, statNm="종묘 공영주차장", chgerId=1, chgerType=3,
            stat=2, addrDoro="경상남도 창원시 마산합포구 구산면 구산로 554", lat=35.119457244873,
            lng=128.580612182617, useTime="24시간 이용가능", LastUsedTime="nodata"
        )

    def test_Charger_model(self):
        self.assertEqual(self.charger1.statNm, '종묘 공영주차장')
