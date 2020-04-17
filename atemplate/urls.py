from django.urls import re_path

from . import views

urlpatterns = [

    re_path(r'template/$', views.CreateTemplate.as_view()),

    ]