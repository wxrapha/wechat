# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-24 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0006_auto_20171024_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='subscribe',
            field=models.BooleanField(default=False, verbose_name='\u5173\u6ce8'),
        ),
    ]
