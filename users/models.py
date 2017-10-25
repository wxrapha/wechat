# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class BlogsWord(models.Model):
    title = models.CharField(max_length=150, verbose_name=u'标题')
    synopsis = models.CharField(max_length=200, verbose_name=u'简介', default='')
    body = UEditorField(verbose_name=u'内容', width=600, height=300, imagePath="myblog/ueditor/", filePath="myblog/ueditor/",
                            default='')
    commit_nums = models.IntegerField(default=0, verbose_name=u'点击数' )
    author = models.CharField(max_length=20, verbose_name=u'作者', default=u'谢昊')
    author_url = models.URLField(verbose_name=u'作者链接', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'编辑时间')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数' )

    class Meta:
        verbose_name = u'博客文章'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名', default='')
    content = models.TextField(verbose_name=u'留言信息')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'留言时间')

    class Meta:
        verbose_name = u'留言'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content


class Life(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    content = UEditorField(verbose_name=u'生活', width=600, height=300, imagePath="myblog/ueditor/", filePath="myblog/ueditor/",
                            default='')

    class Meta:
        verbose_name = u'生活'
        verbose_name_plural = verbose_name


class DescComments(models.Model):
    desc = models.ForeignKey(BlogsWord, verbose_name=u'文章')
    comments = models.CharField(max_length=200, verbose_name=u'评论', default='')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'文章评论'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.comments


