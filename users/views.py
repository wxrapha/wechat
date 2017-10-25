# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from django.views.generic.base import View
from .models import Message, Life, BlogsWord, DescComments
from django.http import HttpResponse
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response


class MessageView(View):
    def get(self, request):
        all_messages = Message.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对留言进行分页
        p = Paginator(all_messages, 8, request=request)

        messages = p.page(page)
        return render(request, 'messages.html', {
            'my_messages': messages
        })


class AddMessagesView(View):
    def post(self, request):
        comments = request.POST.get('message', 0)
        name = request.POST.get('name', 0)
        new_messages = Message()
        new_messages.name = name
        new_messages.content = comments
        new_messages.save()
        return render(request, 'index.html', {})


class LifeView(View):
    def get(self, request):
        life_commits = Life.objects.all().order_by('-add_time')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对生活进行分页
        p = Paginator(life_commits, 8, request=request)

        commits = p.page(page)
        return render(request, 'life.html', {
            'commits': commits
        })


class BlogsWordView(View):
    def get(self, request):
        words = BlogsWord.objects.all().order_by('-add_time')
        #文章搜索
        search_keywords = request.GET.get('keywords', '')
        if search_keywords:
            words = words.filter(Q(title__icontains=search_keywords)|Q(author__icontains=search_keywords)
                                 |Q(synopsis__icontains=search_keywords)|Q(body__icontains=search_keywords))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对文章进行分页
        p = Paginator(words, 8, request=request)

        blogsword = p.page(page)
        return render(request, 'writing.html', {
            'words': blogsword
        })


class DescDetailMessageView(View):
    def post(self, request, contents_id):
        new_comments = request.POST.get('message', 0)
        desc = BlogsWord.objects.get(id=contents_id)
        desc.commit_nums += 1
        desc.save()
        desc_comments = DescComments()
        desc_comments.desc = desc
        desc_comments.comments = new_comments
        desc_comments.save()
        return render(request, 'success.html', {})


class DescDetailView(View):
    def get(self, request, word_id):
        contents = BlogsWord.objects.get(id=int(word_id))

        contents.click_nums += 1
        contents.save()

        all_commits = DescComments.objects.filter(desc=contents)

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # 对留言进行分页
        p = Paginator(all_commits, 5, request=request)

        desc_commits = p.page(page)
        commit_nums = DescComments.objects.all()
        return render(request, 'desc_detail.html', {
            'contents': contents,
            'all_commits': desc_commits,
            'commit_nums': commit_nums
        })


def page_not_found(request):
    #全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    #全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response


def page_wrong(request):
    #全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('403.html', {})
    response.status_code = 403
    return response
