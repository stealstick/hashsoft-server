from django.test import TestCase

from .models import User, UserCarType
# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        self.guest1 = User.objects.create_user(
            username='guest1', email='guest1@gmail.com', password='hashsoft3455',
            year=22, sex="남자", place="서울특별시"
        )
        self.guest2 = User.objects.create_user(
            username='guest2', email='guest2@gmail.com', password='hashsoft3455',
            year = 24, sex = "남자", place = "서울특별시"
        )
        self.guest1.usercartype_set.create(car="소형차")
        self.guest2.usercartype_set.create(car="소형차")
        self.guest2.usercartype_set.create(car="중형차")

    def test_user_cartype_model_check(self):
        """Animals that can speak are correctly identified"""

        self.guest1_car = UserCarType.objects.filter(user=self.guest1)[0]

        self.assertEqual(self.guest1_car.user.username, 'guest1')
        self.assertEqual(self.guest1.usercartype_set.all()[0].car, '소형차')
        self.assertEqual(self.guest2.usercartype_set.all()[0].car, '소형차')
        self.assertEqual(self.guest2.usercartype_set.all()[1].car, '중형차')
