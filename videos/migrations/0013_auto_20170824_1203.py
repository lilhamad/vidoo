# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-24 11:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0012_auto_20170824_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heart',
            name='added_by',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Heart by'),
        ),
    ]
