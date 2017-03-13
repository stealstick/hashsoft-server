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
    serial_number = ''
    for i in range(16):
        serial_number += str(random.randrange(0,9))
    if UserCard.objects.filter(serial_number=serial_number).exists():
        return get_serial_number(depth=depth + 1)
    else:
        return serial_number

class Warnin(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):              # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)
        
class User(AbstractBaseUser, PermissionsMixin):
    SEX_CHOICES = (
        ("남자", "남자"),
        ("여자", "여자"),
    )
    objects = UserManager()
    email = models.CharField(max_length = 40, unique=True)
    username = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined =models.BooleanField(default=True)
    year = models.PositiveIntegerField(default=0, help_text="year")
    sex = models.CharField(max_length=10, help_text="성별", choices=SEX_CHOICES)
    car_type = models.CharField(max_length=300, help_text="차 종류", default="소형차")
    place = models.CharField(max_length=100, help_text="거주지")
    profile = models.ImageField(upload_to=get_upload_path, default="defalutProfileImg.jpg")
    warn= models.ManyToManyField(Warnin)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','year','sex','car_type','place']

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