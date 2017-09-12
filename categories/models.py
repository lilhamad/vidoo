from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField('Category name', max_length=200)
    date_added = models.DateTimeField('Date added', auto_now_add=True)
    added_by = models.ForeignKey(User, verbose_name='The person that added it')

    def __str__(self):
        return self.name