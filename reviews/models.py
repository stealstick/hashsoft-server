from django.db import models

from accounts.models import User
from chargers.models import Charger


class ChargerReview(models.Model):
    charger = models.ForeignKey(Charger, on_delete=models.CASCADE, related_name="review")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="charger_review")
    title = models.TextField()
    text = models.TextField()
    star = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title
