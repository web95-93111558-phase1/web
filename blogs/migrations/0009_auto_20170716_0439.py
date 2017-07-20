# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 00:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20170715_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 16, 0, 9, 40, 31833, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 16, 0, 9, 40, 30833, tzinfo=utc)),
        ),
    ]