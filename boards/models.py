from django.db import models

class Board(models.Model):
    date = models.CharField(max_length=20)
    title = models.CharField(max_length=200,unique=True)
    writer = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.title