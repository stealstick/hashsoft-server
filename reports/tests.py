from django.test import TestCase

from accounts.models import User


class UserForReport(TestCase):

    def setUp(self):
        self.guest1 = User.objects.create_user(
            username='guest1', email='guest1@gmail.com',
            password='hashsoft3455', year=22, sex="남자", place="서울특별시"
        )
        self.guest1.reports.create(title="너무 느려요", content="수정 빨리 좀 해줘요",)

    def test_report(self):
        report = self.guest1.reports.all()[0]
        self.assertEquals(report.title, "너무 느려요")
