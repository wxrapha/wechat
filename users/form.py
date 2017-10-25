# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/9/27 下午4:23'

from django import forms


class MessageForm(forms.Form):
    name = forms.CharField(required=True, min_length=4)
    message = forms.CharField(required=True)