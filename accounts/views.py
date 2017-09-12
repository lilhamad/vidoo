# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from subscriptions.models import Plan, Subscription
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def profile(request, pk):
    user = User.objects.get(id=pk)
    if not hasattr(user, 'subscription'):
        sub = Subscription().save()
    plans = Plan.objects.all()
    return render(request, 'accounts/profile.html', {'user':user, 'plans':plans})


