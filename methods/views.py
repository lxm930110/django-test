from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def login(request, city, year):

    # print('反解析路由:', reverse('login'))
    print('城市名:%s 年份:%s' % (city, year))

    return HttpResponse('拼接参数get请求方式')

def login_query(request):
    params = request.GET
    value1 = params.get('a')
    value2 = params.getlist('b')
    print(value1,value2)
    print(params, type(params))

    # print('反解析路由:', reverse('login'))
    print()

    return HttpResponse('查询参数get请求方式')
