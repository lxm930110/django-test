
from django.conf.urls import url
# from django.contrib import admin
# from django.urls import re_path

from . import views

# app_name = 'haha' 总路由的name可以不写

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='index'),  # 给子路由添加一个name = 'index'
    url(r'^login/$', views.login, name='login'),  # 给子路由添加一个name = 'login'
]