# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-14 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170714_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='G',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defaultBlog', models.IntegerField(null=True)),
            ],
        ),
    ]
