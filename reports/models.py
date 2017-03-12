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
    user = models.ForeignKey(User, related_name="reports")
    title = models.TextField()
    content = models.TextField()
    piture = models.ImageField(blank=True, upload_to=get_upload_path)
