# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-01 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dianzi_weilan', '0009_auto_20180627_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='outblockwarning',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='结束时间'),
        ),
        migrations.AddField(
            model_name='outblockwarning',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='开始时间'),
        ),
    ]
