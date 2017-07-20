# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 18:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20170715_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 15, 18, 36, 1, 322600, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 15, 18, 36, 1, 321600, tzinfo=utc)),
        ),
    ]
