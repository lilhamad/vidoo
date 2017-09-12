# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-18 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20170818_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='details',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='playlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='playlists.Playlist', verbose_name=b'Playlist the video belongs to.'),
        ),
    ]
