from django.test import TestCase

from accounts.models import User
from chargers.models import Charger

# Create your tests here.

class ReviewTestCase(TestCase):
    def setUp(self):
        self.guest1 = User.objects.create_user(
            username='guest1', email='guest1@gmail.com', password='hashsoft3455',
            year=22, sex="남자", place="서울특별시"
        )
        self.charger1 = Charger.objects.create(
            statId=11110003, statNm="종묘 공영주차장", chgerId=1, chgerType=3,
            stat=2, addrDoro="경상남도 창원시 마산합포구 구산면 구산로 554", lat=35.119457244873,
            lng=128.580612182617, useTime="24시간 이용가능", LastUsedTime="nodata"
        )
        self.guest1.charger_review.create(
            title="좋아요!", text="충전도 빠르고 서비스도 주셔서 너무 좋았어요~",
            star=5, charger=self.charger1
            )

    def test_user_reviews_check(self):
        guest1_review1 = self.guest1.charger_review.all()[0]
        charger1_review1 = self.charger1.review.all()[0]
        self.assertEqual(guest1_review1.title, "좋아요!")
        self.assertEqual(guest1_review1.text, "충전도 빠르고 서비스도 주셔서 너무 좋았어요~")

        self.assertEqual(charger1_review1.user.username, "guest1")
        self.assertEqual(charger1_review1.text, "충전도 빠르고 서비스도 주셔서 너무 좋았어요~")


