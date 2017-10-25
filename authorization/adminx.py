# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/9/6 下午8:24'


import xadmin
from .models import Members


class MemberAdmin(object):
    list_display = ['name']


xadmin.site.register(Members, MemberAdmin)
