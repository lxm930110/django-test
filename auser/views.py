from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

# 创建视图函数 1、接受请求对象 2、解析请求对象 3、model,template 4、返回响应对象
from django.urls import reverse



def index(request):
    # 返回响应对象
    return HttpResponse('第一次使用Django框架....')


def login(request):

    m = reverse('index')
    # 返回响应对象
    # return HttpResponse('这是一个登录页面....')
    return redirect(m)