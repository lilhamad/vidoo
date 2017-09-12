# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from subscriptions.models import Subscription, Plan, Payment

# Register your models here.

admin.site.register(Subscription)
admin.site.register(Plan)
admin.site.register(Payment)
