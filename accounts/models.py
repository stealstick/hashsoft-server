import os
import random
import time

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.dispatch import receiver


def get_upload_path(instance, filename):
    currently = time.strftime("%y%m%d%H%M%S")
    return os.path.join(
      "profile" , "{}_{}.jpg".format(currently, instance.username)
    )

def get_serial_number(depth=0):
    serial_number = '10100100'
    for i in range(8):
        serial_number += str(random.randrange(0,9))
    if UserCard.objects.filter(serial_number=serial_number).exists():
        return get_serial_number(depth=depth + 1)
    else:
        return serial_number


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    email = models.CharField(max_length = 40, unique=True)
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined =models.BooleanField(default=True)
    year = models.PositiveIntegerField(default=0, help_text="year")
    phone_number = models.CharField(max_length=15)
    profile = models.ImageField(upload_to=get_upload_path, default="defalutProfileImg.jpg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','year']

    def __str__(self):
        return '%s' % self.email

    def get_short_name(self):
        return self.username

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        try:
            user_card = getattr(self, "user_card")
        except AttributeError:
            UserCard(user=self).save()


class Comaccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    com = models.CharField(max_length=50, default=get_serial_number, unique=True)
    userid = models.CharField(max_length=50, default=get_serial_number, unique=True)
    userpw = models.CharField(max_length=50, default=get_serial_number, unique=True)

class UserCard(models.Model):
    user = models.OneToOneField(User,related_name="user_card", on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=20, default=get_serial_number, unique=True)
    balance = models.BigIntegerField(default=0)

@receiver(models.signals.post_delete, sender=User)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.profile:
        if os.path.isfile(instance.profile.path):
            os.remove(instance.profile.path)

@receiver(models.signals.pre_save, sender=User)
def auto_delete_file_on_change(sender, instance, **kwargs):
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
            os.remove(old_file.path)
