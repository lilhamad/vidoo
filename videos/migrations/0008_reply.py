# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-23 09:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0007_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name=b'reply')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name=b'Replied on')),
                ('added_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'Replied by')),
                ('comment', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='videos.Comment', verbose_name=b'Comment')),
            ],
        ),
    ]