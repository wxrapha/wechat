# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Members(models.Model):
    name = models.CharField(verbose_name=u'用户', max_length=128, default='')
    sex = models.CharField(choices=((1, u'男'), (0, u'女')),default=0, max_length=20, verbose_name=u'性别')
    province = models.CharField(max_length=128, verbose_name=u'省市')
    country = models.CharField(max_length=128, verbose_name=u'国家')
    city = models.CharField(max_length=128, verbose_name=u'城市')
    openid = models.CharField(verbose_name=u'openid',default=0, max_length=30)
    birthday = models.DateTimeField(auto_now_add=True,blank=True, null=True, verbose_name=u'生日')
    realname = models.CharField(verbose_name=u'真实姓名', max_length=128, default='')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号')
    address = models.CharField(verbose_name=u'地址', max_length=128, default='')
    industry = models.CharField(verbose_name=u'行业', max_length=128, default='')
    company = models.CharField(verbose_name=u'公司', max_length=128, default='')
    position = models.CharField(verbose_name=u'职位', max_length=128, default='')
    subscribe = models.BooleanField(verbose_name=u'关注', default=False)
    subscribe_time = models.DateTimeField(auto_now_add=True,blank=True, null=True, verbose_name=u'关注时间')
    headimgurl = models.CharField(default ='', max_length=128, verbose_name=u'用户头像url')

    class Meta:
        verbose_name = u'成员'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name







