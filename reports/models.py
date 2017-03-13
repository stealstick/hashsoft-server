import os
import time

from django.db import models

from accounts.models import User


def get_upload_path(instance, filename):
    currently = time.strftime("%y%m%d%H%M%S")
    return os.path.join(
      "reports" , "{}_{}.jpg".format(currently, instance.user.username)
    )

class Report(models.Model):
    STATUS_CHOICE = (
        ("0", "대기 중"),
        ("1", "처리 중"),
        ("2", "처리 완료"),
        ("3", "보류")
    )
    user = models.ForeignKey(User, related_name="reports")
    title = models.TextField()
    content = models.TextField()
    status = models.CharField(max_length=10,choices=STATUS_CHOICE, default=0)
    piture = models.ImageField(blank=True, upload_to=get_upload_path)
