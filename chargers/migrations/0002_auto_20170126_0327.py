# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chargers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charger',
            name='statId',
            field=models.CharField(max_length=100),
        ),
    ]
