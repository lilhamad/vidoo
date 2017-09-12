from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
# Create your models here.


class Playlist(models.Model):
    name = models.CharField('Playlist name', max_length=200)
    date_added = models.DateTimeField('Date added', auto_now_add=True)
    category = models.ForeignKey(Category, null=True)
    added_by = models.ForeignKey(User, verbose_name='Added by')

    def __str__(self):
        return self.name