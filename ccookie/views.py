from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def set_cookie_fun(request):

    # 获取cookie的value
    result = request.COOKIES.get('itcast')
    print(result)


    response = HttpResponse('设置cookies')
    # 设置cookie的值
    response.set_cookie('itcast', 'itheima',max_age=10)

    return response