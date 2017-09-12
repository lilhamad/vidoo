from . import views
from django.conf.urls import url

app_name = 'subs'
urlpatterns = [
    url(r'^pay/$', views.pay, name='pay'),
    url(r'^(?P<pk>[0-9]+)/pay/$', views.pay, name='pay'),
]