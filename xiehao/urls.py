# -*- coding:utf-8 -*-
"""xiehao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
import xadmin
from users.views import MessageView, AddMessagesView, LifeView, BlogsWordView, \
    DescDetailView, DescDetailMessageView
from xiehao.settings import MEDIA_ROOT
from django.views.static import serve
from robot import robot
from werobot.contrib.django import make_view
from xiehao import tests
from wechat import wechat
from authorization import views

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^wechat/', views.index, name='wechat'),
    url(r'^wechat_info/$', views.info, name="wechat_info"),
   # url('^robot/$', make_view(robot), name='index'),
    url(r'^code$', views.get_code, name='get_code'),
    url(r'^web_auth/$', views.web_auth, name='web_auth'), 
    url(r'^allfans/$',views.AllFansView.as_view(), name='allfans'),
    url(r'^fansdetail/(?P<fan_id>\d+)/$', views.FansDetailView.as_view(), name='fansdetail'),   	
    # 配置上传文件访问地址
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),

    url(r'^aboutme/$', TemplateView.as_view(template_name='about_me.html'), name='about_me'),

    url(r'^writing/$', BlogsWordView.as_view(), name='writing'),

    url(r'^favourite/$', TemplateView.as_view(template_name='favourite.html'), name='favourite'),
    #评论页
    url(r'^messages/$', MessageView.as_view(), name='messages'),
    #添加评论
    url(r'^add_messages/$', AddMessagesView.as_view(), name='add_messages'),
    url(r'^add_desc_commit/(?P<contents_id>\d+)', DescDetailMessageView.as_view(), name='add_desc_commit'),

    url(r'^life/$', LifeView.as_view(), name='life'),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^word/(?P<word_id>\d+)$', DescDetailView.as_view(), name='desc'),

]
