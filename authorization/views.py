# -*- coding: utf-8 -*-
import hashlib
import time
import urllib
import json
import logging

from django.views.generic.base import View
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from rest_framework.decorators import api_view
from wechatpy import parse_message, create_reply
from .models import Members
from xiehao.settings import appID, appsecret, Token

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST'])
def index(request):
    """
    微信简单通信，
    GET用于验证签名信息，
    加密/校验流程如下：
    1. 将token、timestamp、nonce三个参数进行字典序排序
    2. 将三个参数字符串拼接成一个字符串进行sha1加密
    3. 开发者获得加密后的字符串可与signature对比，标识该请求来源于微信
    POST实现一个简单的回复信息
    """
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        tmp_list = [Token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("请用微信")

    if request.method == 'POST':
       # data = request.data
       # toUserName = data.get('ToUserName', '')
       # fromUserName = data.get('FromUserName', '')
       # msgType = data.get('MsgType', '')
        msg = parse_message(request.body)
	if msg.type == 'event':
	    if msg.event == 'subscribe':
	        reply = create_reply('谢谢关注', msg)
		openid = msg.source
		print openid
		
		print subscriber
		try:
		    subscriber = Members.objects.get(openid=openid)
		    subscriber.subscribe = True
		    subscriber.save()
		except:
		    new_subscribr = Members()
		    new_subscribr.openid = openid
		    new_subscribr.save()
	
	    elif msg.event == 'unsubscribe':
		openid = msg.source
		unsubscriber = Members.objects.get(openid=openid)
	        print unsubscriber
		unsubscriber.subscribe = False
		unsubscriber.save()

	
	elif msg.type == 'text':
	    reply = create_reply(msg.source, msg)
	elif msg.type == 'image':  
            reply = create_reply('这是条图片消息', msg)  
        elif msg.type == 'voice':  
            reply = create_reply('这是条语音消息', msg) 
	else:
	    reply = create_reply('其他类型消息暂无逻辑', msg)
	response = HttpResponse(reply.render(), content_type="application/xml")
	return response


def web_auth(request):
    """
    网页提示是否授权

    """
    if request.method == 'GET':
        return render(request, 'web_auth.html')
    if request.method == 'POST':

        flag = int(request.POST.get('flag', 0))   # flag 表示是否同意授权 1/0
        if flag:
            data = urllib.urlencode({
                'appid': appID,
                'redirect_uri': 'http://'+ request.get_host() + reverse('get_code'),
                'response_type': 'code',
                'scope': 'snsapi_userinfo',
                'state': 'STATE_one',
            })
            redirect_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?' + \
                data + '#wechat_redirect'
            return redirect(redirect_url)         # 同意授权则跳转到获取code
	    print redirect_url
        else:
            return redirect(reverse('web_auth'))

def get_code(request):
    """
    用户授予权限，获取code，通过code获取access_toekn, 再通过access_token获取用户信息
    """
    if request.method == 'GET':
        state = request.GET.get('state', '')
        print state
        if state == 'STATE_one':
            code = request.GET.get('code', '')
            if code:
            # 第二步：通过code换取网页授权access_token
                try:
                    response = urllib.urlopen(url='https://api.weixin.qq.com/sns/oauth2/access_token',
                                          data=urllib.urlencode({
                                              'appid': appID,
                                              'secret': appsecret,
                                              'code': code,
                                              'grant_type': 'authorization_code',
                                          })
                                          )
                except Exception, reson:
                    logger.exception(u'调用微信api失败[%s]！', reson)
                    return render(request, 'error.html')

                response_dic = json.loads(response.read())          # 解析json
                errcode = response_dic.get('errcode', None)         # 调用失败
                if errcode:
                    # raise 错误原因
                    logger.exception(
                        u'调用微信api失败[%d:%s]！', errcode, response_dic.get('errmsg', ''))
                    return render(request, 'error.html')

                access_token = response_dic.get('access_token', '')
                openid = response_dic.get('openid', '')
		print openid
                # 第四步：拉取用户信息(需scope为 snsapi_userinfo), 使用到access_token, openid
                info_url = 'https://api.weixin.qq.com/sns/userinfo'
                try:
                    info_response = urllib.urlopen(url=info_url,
                                               data=urllib.urlencode({
                                                   'access_token': access_token,
                                                   'openid': openid,
                                                   # 默认使用中文吧
                                                   'lang': 'zh_CN'
                                               })
                                               )
                except Exception, reson:
                    logger.exception(u'调用微信api失败[%s]！', reson)
                    return render(request, 'error.html')

                info_dic = json.loads(info_response.read())          # 解析json
	        errcode = info_dic.get('errcode', None)              # 调用失败
                if errcode:
                    # raise 错误原因
                    logger.exception(
                        u'调用微信api失败[%d:%s]！', errcode, response_dic.get('errmsg', ''))
                    return render(request, 'error.html')

                nickname = info_dic.get('nickname', '')              # 昵称
                sex = info_dic.get('sex', 1)                         # 性别
                province = info_dic.get('province', '')              # 省
                country = info_dic.get('country', '')                # 国家
                city = info_dic.get('city', '')                      # 城市
                headimgurl = info_dic.get('headimgurl', '')          # 头像url
	#	subscribe_time = info_dic['subscribe_time']
	#	subscribe = info_dic['subscribe']
	#	print subscribe_time
 	#	print subscribe  		
		
		
                
		print members
                try:
		    members = Members.objects.get(openid=openid)
                    members.name = nickname
		    print members.name
                    members.sex = sex
                    members.province = province
                    members.country = country
                    members.city = city
              	    members.openid = openid
		    members.headimgurl = headimgurl
                    members.save()
		except:
		    new_members = Members()
		    new_members.name = nickname
		    print new_members.name
                    new_members.sex = sex
                    new_members.province = province
                    new_members.country = country
                    new_members.city = city
                    new_members.openid = openid
                    new_members.headimgurl = headimgurl
                    new_members.save()    

                return render(request, 'user_info.html',
                          {
                              'nickname': nickname,
                              'sex': sex,
                              'province': province,
                              'country': country,
                              'city': city,
                              'headimgurl': headimgurl,
                          },
                          )
        if state == 'STATE_two':
            code = request.GET.get('code', '')
            print code
            if code:
            # 第二步：通过code换取网页授权access_token

                response = urllib.urlopen(url='https://api.weixin.qq.com/sns/oauth2/access_token',
                                          data=urllib.urlencode({
                                              'appid': appID,
                                              'secret': appsecret,
                                              'code': code,
                                              'grant_type': 'authorization_code',
                                          })
                                          )


                response_dic = json.loads(response.read())  # 解析json
		access_token = response_dic.get('access_token', '')
		print access_token
                openid = response_dic.get('openid', None)
                print openid

                userinfo = Members.objects.get(openid=openid)
                print userinfo

                return render(request, 'wechat_info.html',{
                    'userinfo':userinfo
                })


def info(request):
        """
        网页base授权, 获取openid

        """
        if request.method == 'GET':
            data = urllib.urlencode({
                    'appid': appID,
                    'redirect_uri': 'http://'+ request.get_host() + reverse('get_code'),
                    'response_type': 'code',
                    'scope': 'snsapi_base',
                    'state': 'STATE_two',
                })
            redirect_url = 'https://open.weixin.qq.com/connect/oauth2/authorize?' + \
                               data + '#wechat_redirect'
	    print redirect_url
            return redirect(redirect_url)  # 静默授权跳转获取code
	if request.method == 'POST':
	    realname = request.POST.get('realname', '')
	    print realname
	    mobile = request.POST.get('mobile', '')
	    openid = request.POST.get('openid', None)
	    print openid
	    birthday = request.POST.get('birthday', '')
	    print birthday
	    address = request.POST.get('address', '')
	    industry = request.POST.get('industry', '')
	    company = request.POST.get('company', '')
	    position = request.POST.get('position', '')
	    try:
	        wechat_info = Members.objects.get(openid=openid)
	        print wechat_info
	        wechat_info.realname = realname
	        wechat_info.mobile = mobile
	        wechat_info.address = address
	        wechat_info.industry = industry
	        wechat_info.company = company
	        wechat_info.position = position
	        wechat_info.birthday = birthday
	        wechat_info.save()
	        return render(request, 'success.html')
	    ecxept:
		return HttpResponse("请用微信")

class AllFansView(View):
    def get(self, request):
	fans = Members.objects.filter(subscribe=True)
	print fans
	return render(request, 'allfans.html', {
			'fans':fans
			})


class FansDetailView(View):
    def get(self, request, fan_id):
	fan = Members.objects.get(id=int(fan_id))
	return render(request, 'fansdetail.html', {
			'fan':fan
			})
