# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-24 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0007_members_subscribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='birthday',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u751f\u65e5'),
        ),
        migrations.AddField(
            model_name='members',
            name='subscribe_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u5173\u6ce8\u65f6\u95f4'),
        ),
    ]