from django.test import TestCase

from .models import Caveat, CaveatManager
from accounts.models import User

class CaveatModelTest(TestCase):

    def setUp(self):
        self.guest1 = User.objects.create_user(
            username='guest1', email='guest1@gmail.com', password='hashsoft3455',
            year=22, sex="남자", place="서울특별시"
        )
        self.caveat1 = Caveat.objects.create(title="못생김")
        CaveatManager.objects.create(user=self.guest1, caveat=self.caveat1)

    def test_cavate_count(self):
        user = self.guest1
        try:
            caveat=CaveatManager.objects.get(user=user, caveat=self.caveat1)
        except CaveatManager.DoesNotExist:
            return
        caveat.count+=1
        caveat.save()
        self.assertEquals(caveat.count, 2)
