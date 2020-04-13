from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^login/(?P<year>\d{4})/(?P<city>[a-z]+)/$', views.login, name='login'),
    url(r'^login_query/$', views.login_query, name='login'),
    url(r'^login_form/$', views.login_form),
    url(r'^login_not_form/$', views.login_not_form),
    url(r'^login_headers/$', views.login_headers),
]