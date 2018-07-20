# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-12-04 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockPolygon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=300, verbose_name='\u5197\u957f\u540d\u5b57')),
                ('name', models.CharField(max_length=100, verbose_name='\u540d\u5b57')),
                ('display', models.TextField(verbose_name='\u663e\u793a\u591a\u8fb9\u5f62')),
                ('bounding', models.TextField(verbose_name='\u63a2\u6d4b\u591a\u8fb9\u5f62')),
            ],
        ),
    ]
