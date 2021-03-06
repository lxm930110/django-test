"""zdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import url, include

from django.contrib import admin
from django.conf.urls import url, include

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r'admin/', admin.site.urls),

    path(r'auser/', include('auser.urls')),
    # request五种请求子应用
    path(r'', include('methods.urls')),
    # response子应用
    path(r'', include('cresponse.urls')),
    # cookie子运用
    path(r'', include('ccookie.urls')),
    # session子运用
    path(r'', include('csession.urls')),
    # add_decorator子运用
    path(r'', include('add_decorator.urls')),
    # 添加模板
    path(r'', include('atemplate.urls')),
    # 添加数据库子应用
    path(r'', include('dbtest.urls')),


]
