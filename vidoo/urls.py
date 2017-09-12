"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import logout
from videos.views import login, index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index.as_view(), name='index'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^videos/', include('videos.urls')),
    url(r'^subs/', include('subscriptions.urls')),
    url(r'^categories/', include('categories.urls')),
    url(r'^login$', login, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': reverse_lazy('videos:index')}, name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)