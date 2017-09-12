from django.db import models
from django.contrib.auth.models import User
from playlists.models import Playlist
from categories.models import Category
from django.core.urlresolvers import reverse
from .get_request import get_request
# Create your models here.


class Video(models.Model):
    name = models.CharField(max_length=200)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, verbose_name='Playlist', null=True)
    category = models.ForeignKey(Category, verbose_name='Category')
    date_added = models.DateTimeField('Date added', auto_now_add=True)
    added_by = models.ForeignKey(User, verbose_name='Added by', editable=False)
    path = models.FileField('Select', max_length=250)
    details = models.CharField(null=True, max_length=400)
    extension = models.CharField('Extension', max_length=20)
    view_count = models.IntegerField('Views', default=0)

    def save(self):
        request = get_request()
        self.added_by = request.user
        self.extension = self.path.url[-4:].strip('.')
        super(Video, self).save()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('videos:detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    video = models.ForeignKey(Video, verbose_name='Video', editable=False)
    text = models.TextField('comment', null=False)
    added_by = models.ForeignKey(User, editable=False, verbose_name='Posted by')
    date_added = models.DateTimeField('Posted on', auto_now_add=True)

    def save(self):
        request = get_request()
        self.added_by = request.user
        super(Comment, self).save()

    def __str__(self):
        return self.text[:40]


class Reply(models.Model):
    comment = models.ForeignKey(Comment, verbose_name='Comment', editable=False)
    text = models.TextField('reply', null=False)
    added_by = models.ForeignKey(User, editable=False, verbose_name='Replied by')
    date_added = models.DateTimeField('Replied on', auto_now_add=True)

    def save(self):
        request = get_request()
        self.added_by = request.user
        super(Reply, self).save()

    def __str__(self):
        return self.text[:40]


class Watch(models.Model):
    video = models.ForeignKey(Video, verbose_name='Video', editable=False)
    added_by = models.ForeignKey(User, editable=False, verbose_name='Watched by')
    date_added = models.DateTimeField('Watched on', auto_now_add=True)

    def save(self):
        request = get_request()
        self.added_by = request.user
        super(Watch, self).save()


    def __str__(self):
        return self.video[:20]


class Like(models.Model):
    video = models.ForeignKey(Video, verbose_name='Video', editable=False)
    added_by = models.ForeignKey(User, editable=False, verbose_name='Liked by')
    date_added = models.DateTimeField('Liked on', auto_now_add=True)

    def save(self):
        request = get_request()
        self.added_by = request.user
        super(Like, self).save()


class Dislike(models.Model):
    video = models.ForeignKey(Video, verbose_name='Video', editable=False)
    added_by = models.ForeignKey(User, verbose_name='Disliked by')
    date_added = models.DateTimeField('Disliked on', auto_now_add=True)

    def save(self):
        request = get_request()
        self.added_by = request.user
        super(Dislike, self).save()


    def __str__(self):
        return self.video


class Heart(models.Model):
    comment = models.ForeignKey(Comment, verbose_name='Comment', editable=False)
    added_by = models.ForeignKey(User, editable=False, verbose_name='Heart by')
    date_added = models.DateTimeField('Heart on', auto_now_add=True)

    def save(self):
        request = get_request()
        self.added_by = request.user
        super(Heart, self).save()

    def __str__(self):
        return self.added_by.username
