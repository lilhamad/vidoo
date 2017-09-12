from . import views
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

app_name = 'categories'
urlpatterns = [
    url(r'^create/$', login_required(views.create.as_view()), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.show, name='detail'),
]