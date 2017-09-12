# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from videos.models import Video, Comment, Reply, Watch, Like, Heart, Dislike

# Register your models here.


admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Watch)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Heart)
