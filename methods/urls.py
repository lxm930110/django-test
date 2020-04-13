from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^login/(?P<year>\d{4})/(?P<city>[a-z]+)/$', views.login, name='login'),
    url(r'^login_query/$', views.login_query, name='login'),
]