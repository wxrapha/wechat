# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/9/6 下午8:24'


import xadmin
from .models import BlogsWord, Message, Life, DescComments


class BlogsWordAdmin(object):
    list_display = ['title',  'add_time']
    style_fields = {'body': 'ueditor'}


class MessageAdmin(object):
    list_display = ['content', 'add_time']


class LifeAdmin(object):
    list_display = ['content']
    style_fields = {'content': 'ueditor'}


class DescCommentsAdmin(object):
    list_display = ['desc', 'add_time']

xadmin.site.register(BlogsWord, BlogsWordAdmin)
xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(Life, LifeAdmin)
xadmin.site.register(DescComments, DescCommentsAdmin)
