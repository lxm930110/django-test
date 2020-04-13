import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

# 拼接路径传参
def login(request, city, year):


    print('城市名:%s 年份:%s' % (city, year))


    return HttpResponse('拼接路径get请求方式')

# 查询字符串方式传参
def login_query(request):

    params = request.GET
    value1 = params.get('a')
    value2 = params.getlist('b')
    print(value1,value2)
    print(params, type(params))

    return HttpResponse('查询参数get请求方式')

# 表单类型传值
def login_form(request):

    params = request.POST
    value1 = params.get('a')
    value2 = params.getlist('b')
    print(value1, value2)
    # print(params, type(params))

    return HttpResponse('login_form')


# 非表单类型传值
def login_not_form(request):
    # 参数为json格式 把二进制转字符串再转字典
    result = request.body
    print(result, type(result))

    result_str = result.decode()
    print(result_str, type(result_str))

    result_dict = json.loads(result_str)
    print(result_dict, type(result_dict))

    return HttpResponse('非表单类型传值')


# 请求头信息
def login_headers(request):

    print(request.method)
    print(request.path)
    # print(request.META)
    print(request.META['CONTENT_TYPE'])


    return HttpResponse('请求头的请求方式：login_headers')
