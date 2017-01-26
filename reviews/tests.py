from django.test import TestCase

from accounts.models import User
from .models import Review

# Create your tests here.

class ReviewTestCase(TestCase):
    def setUp(self):
        self.guest1 = User.objects.create_user(
            username='guest1', email='guest1@gmail.com', password='hashsoft3455',
            year=22, sex="남자", place="서울특별시"
        )
        self.guest2 = User.objects.create_user(
            username='guest2', email='guest2@gmail.com', password='hashsoft3455',
            year=24, sex="남자", place="서울특별시"
        )
        self.guest1.review_set.create(
            title="좋아요!", text="충전도 빠르고 서비스도 주셔서 너무 좋았어요~",
            star=5
            )

    def test_user_reviews_check(self):
        guest1_review1 = self.guest1.review_set.all()[0]
        self.assertEqual(guest1_review1.title, "좋아요!")
        self.assertEqual(guest1_review1.text, "충전도 빠르고 서비스도 주셔서 너무 좋았어요~")
