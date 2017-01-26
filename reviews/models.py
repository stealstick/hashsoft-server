from django.db import models

from accounts.models import User
# Create your models here.

class Review(models.Model):
    review_number = models.AutoField(primary_key=True, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    text = models.TextField()
    star = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title