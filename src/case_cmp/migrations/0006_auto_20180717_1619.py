# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-17 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_cmp', '0005_auto_20180717_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='jianducase',
            name='deptcode',
            field=models.CharField(default='', help_text='赵巷：20601', max_length=10, verbose_name='主责部门'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jianducase',
            name='executedeptcode',
            field=models.CharField(blank=True, help_text='赵巷：20601', max_length=20, verbose_name='三级主责部门'),
        ),
    ]
