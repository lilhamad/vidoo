# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required()
def show(request, pk):
    category = get_object_or_404(Category, pk=pk)
    videos = []
    for playlist in category.playlist_set.all().order_by('-date_added'):
        videos += playlist.video_set.all().order_by()[:1]
    return render(request, 'videos/index.html', {'videos': videos})


class create(CreateView):
    model = Category
    fields = ['name', 'playlist', 'category', 'path', 'details']
