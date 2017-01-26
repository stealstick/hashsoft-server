import time
import os

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

from chargers.models import Charger


def get_upload_path(instance, filename):
    currently = time.strftime("%y%m%d%H%M%S")
    return os.path.join(
      "media","profile" , "{}_{}.jpg".format(currently, instance.username)
    )

class User(AbstractUser):
    year = models.PositiveIntegerField(default=0, help_text="year")
    sex = models.CharField(max_length=10, help_text="성")
    place = models.CharField(max_length=100, help_text="거주지")
    fav = models.ManyToManyField(Charger)
    profile = models.ImageField(upload_to=get_upload_path)


class UserCarType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.CharField(max_length=10, help_text="차종")


@receiver(models.signals.post_delete, sender=User)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `User` object is deleted.
    """
    if instance.profile:
        if os.path.isfile(instance.profile.path):
            os.remove(instance.profile.path)

@receiver(models.signals.pre_save, sender=User)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `User` object is changed.
    """
    try:
        old_file = User.objects.get(pk=instance.pk).profile.path
    except User.DoesNotExist:
        return False


    if not instance.pk:
        return False

    try:
        old_file = User.objects.get(pk=instance.pk).profile
    except User.DoesNotExist:
        return False

    new_file = instance.profile
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
