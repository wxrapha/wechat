# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-24 16:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0008_auto_20171024_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='headimgurl',
            field=models.CharField(default='', max_length=128, verbose_name='\u7528\u6237\u5934\u50cfurl'),
        ),
    ]
