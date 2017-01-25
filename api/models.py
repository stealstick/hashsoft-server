from django.db import models

class board(models.Model):
    date = models.CharField(max_length=20)
    title = models.TextField()
    writer = models.CharField(max_length=20)
    content = models.TextField()