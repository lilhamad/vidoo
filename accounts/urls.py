from . import views
from django.conf.urls import url

app_name = 'accounts'
urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/profile/$', views.profile, name='profile'),
]