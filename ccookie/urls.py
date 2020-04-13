from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^cookie/$', views.set_cookie_fun),
    # url(r'^json_response/$', views.json_response),
]