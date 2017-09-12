from . import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

app_name = 'videos'
urlpatterns = [
    url(r'^$', views.index.as_view(), name='index'),
    url(r'^create/$', login_required(views.create.as_view()), name='create'),
    url(r'^(?P<pk>[0-9]+)/create_comment/$', login_required(views.create_comment), name='create_comment'),
    url(r'^create_comment/$', login_required(views.create_comment), name='create_comment'),
    url(r'^(?P<pk>[0-9]+)/create_reply/$', login_required(views.create_reply), name='create_reply'),
    url(r'^(?P<pk>[0-9]+)/create_like/$', login_required(views.create_like), name='create_like'),
    url(r'^(?P<pk>[0-9]+)/create_dislike/$', login_required(views.create_dislike), name='create_dislike'),
    url(r'^(?P<pk>[0-9]+)/create_heart/$', login_required(views.create_heart), name='create_heart'),
    url(r'^(?P<pk>[0-9]+)/$', views.show, name='detail'),
]