from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^object_response/$', views.object_response),
    url(r'^json_response/$', views.json_response),
]