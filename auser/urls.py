
from django.conf.urls import url
# from django.contrib import admin
# from django.urls import re_path

from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),
    url(r'^login/$', views.login),
]