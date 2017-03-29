from django.db import models


class Board(models.Model):
    date = models.CharField(max_length=20, help_text="게시판 작성 날짜")
    title = models.CharField(max_length=200, unique=True, help_text="게시판 제목")
    writer = models.CharField(max_length=20, help_text="게시판 작성자")
    content = models.TextField(help_text="게시판 내용")

    def __str__(self):
        return self.title

class Dataroom(models.Model):
    date = models.CharField(max_length=20, help_text="게시판 작성 날짜")
    title = models.CharField(max_length=200, unique=True, help_text="게시판 제목")
    writer = models.CharField(max_length=20, help_text="게시판 작성자")
    filelink = models.CharField(max_length=200, help_text="자료실 파일 링크")
    content = models.TextField(help_text="게시판 내용")

    def __str__(self):
        return self.title