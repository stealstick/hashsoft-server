from django.test import TestCase

from .models import Board

class BoardTestCase(TestCase):
    def setUp(self):
        self.board1 = Board.objects.create(
            date = "2016-01-15", title="충전소 추가", writer="장준영",
            content="서울특별시 송파구 삼전동에 전기 자동차 충전소가 생성되었습니다."
        )

    def test_Charger_model(self):
        self.assertEqual(self.board1.writer, '장준영')
