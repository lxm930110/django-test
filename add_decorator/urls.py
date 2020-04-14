
from django.urls import re_path

from . import views

urlpatterns = [

    re_path(r'^add_decorator/$', views.DecoratorFun.as_view()),
    # 直接在把视图函数当成参数传给装饰器函数，这样也可以达到给类视图里面方法添加装饰，但是此方法不便于阅读代码
    # re_path(r'^add_decorator1/$', views.my_decorator(views.DecoratorFun.as_view())),

    ]