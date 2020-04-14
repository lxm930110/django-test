from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


# 创建类视图
class SessionView(View):
    # get方法
    def get(self, request):
        # 设置session的值
        request.session['itcast'] = 'python'
        # 获取session的值
        value = request.session.get('itcast')
        print(value)

        return HttpResponse('get/SessionView')

    # post方法
    def post(self, request):
        # 设置session的值
        request.session['itcast'] = 'python'
        # 获取session的值
        value = request.session.get('itcast')
        print(value)

        return HttpResponse('post/SessionView')


