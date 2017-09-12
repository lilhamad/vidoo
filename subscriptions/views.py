# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from subscriptions.models import Plan, Subscription, Payment
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required()
def pay(request):
    if request.method == 'POST':
        plan = Plan.objects.get(pk=request.POST['value'])
        videoid = request.POST['videoid']

        sub = request.user.subscription
        sub.value += plan.number
        sub.save()

        pay = Payment(amount=plan.amount, account=request.POST['account'])
        pay.save()
        plans = Plan.objects.all()
        return HttpResponseRedirect('/accounts/'+str(request.user.id)+'/profile?link=subed&videoid='+str(videoid))
