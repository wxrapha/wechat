# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-24 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0005_auto_20171023_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='sex',
            field=models.CharField(choices=[(1, '\u7537'), (0, '\u5973')], default=0, max_length=20, verbose_name='\u6027\u522b'),
        ),
    ]
