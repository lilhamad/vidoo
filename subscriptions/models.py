# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from videos.get_request import get_request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subscription(models.Model):
    value = models.IntegerField('Video remaining', default=0)
    date_added = models.DateTimeField('Subscribed on', auto_now_add=True)
    added_by = models.OneToOneField(User, editable=False, verbose_name='Subscriber')


    def save(self):
        request = get_request()
        self.added_by = request.user
        super(Subscription, self).save()


    def __str__(self):
        return self.added_by.username


class Payment(models.Model):
    account = models.IntegerField('Account')
    added_by = models.ForeignKey(User, verbose_name='Pay by')
    date_added = models.DateTimeField(auto_now_add=True)
    subscription_code = models.SlugField()
    amount = models.IntegerField()

    def save(self):
        request = get_request()
        self.added_by = request.user
        super(Payment, self).save()


    def __str__(self):
        return self.added_by.username


class Plan(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    dae_added = models.DateTimeField('Added on', auto_now_add=True)
    added_by = models.ForeignKey(User)
    amount = models.IntegerField()

    def save(self):
        request = get_request()
        self.added_by = request.user
        super(Plan, self).save()


    def __str__(self):
        return self.name