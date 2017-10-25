# _*_ coding: utf-8 _*_
__author__ = 'xiehao'
__date__ = '2017/9/27 下午4:06'

from django.core.cache import cache
from .models import Message


def get_message_cache():
    key = 'id'
    if cache.has_key(key):
        data = cache.get(key)
    else:
        data = get_message_data()

        cache.set(key, data, 10*60)
    return data


def get_message_data():
    data = Message.objects.all()
    return data