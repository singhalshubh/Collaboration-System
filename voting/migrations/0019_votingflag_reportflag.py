# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-14 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0018_auto_20180614_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingflag',
            name='reportflag',
            field=models.BooleanField(default=False),
        ),
    ]
