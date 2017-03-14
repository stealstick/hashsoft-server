from django.db import models

from accounts.models import User


class Caveat(models.Model):
    title = models.CharField(max_length=100, unique=True)
    users = models.ManyToManyField(User, through='CaveatManager',
                                   related_name="caveats")

    def __str__(self):
        return "<%s %s>" % (self.__class__.__name__, self.title)


class CaveatManager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caveat = models.ForeignKey(Caveat, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return "%s-%s-%s" % (self.user.email,
                             self.caveat.title,
                             self.count)
