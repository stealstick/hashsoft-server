from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    year = models.PositiveIntegerField(default=0, help_text="year")
    sex = models.CharField(max_length=10, help_text="성")
    place = models.CharField(max_length=100, help_text="거주지")


class UserCarType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.CharField(max_length=10, help_text="차종")

