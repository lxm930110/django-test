from django.urls import re_path

from . import views

urlpatterns = [

    re_path(r'^csession/$', views.SessionView.as_view()),

    ]