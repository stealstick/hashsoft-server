# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
