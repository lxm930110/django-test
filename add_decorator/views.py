from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View

# 定义一个装饰器
def my_decorator(fn):

    def wrapper(request, *args, **kwargs):
        print('给类视图里面的方法添加装饰器')
        # 输出一下请求方式
        print(request.method)
        return fn(request, *args, **kwargs)
    return wrapper


# 直接在子路由里面提加装饰器不修改类视图
# class DecoratorFun(View):
#
#     def get(self, request):
#         return HttpResponse('类视图中的get方法')
#
#     def post(self, request):
#         # print(request.method.lower())
#
#         return HttpResponse('类视图中的post方法')


# 给对应的方法添加装饰器，再通过给装饰器内部函数的参数添加一个self，也可以达到效果
# class DecoratorFun(View):
#     @my_decorator
#     def get(self, request):
#         return HttpResponse('类视图中的get方法')
#
#     @my_decorator
#     def post(self, request):
#         # print(request.method.lower())
#
#         return HttpResponse('类视图中的post方法')



'''利用django框架自带的@method_decorator实现给class直接装饰
    name = 'dispatch'给类里面所有方法添加装饰器
'''
@method_decorator(my_decorator, name='dispatch')
class DecoratorFun(View):

    def get(self, request):

        return HttpResponse('类视图中的get方法')

    def post(self, request):

        # print(request.method.lower())

        return HttpResponse('类视图中的post方法')

