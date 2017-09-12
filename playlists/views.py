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
    videos = category.video_set.all()
    return render(request, 'videos/index.html', {'videos': videos})




class create(CreateView):
    model = Video
    fields = ['name', 'playlist', 'category', 'path', 'details']


def login(request):
    from django.contrib.auth import login as auth_login
    if '=' in request.POST.get('next', ''):
        a, next_page = request.POST.get('next', '').split('=')
    else:
        next_page = request.POST.get('next', '')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                if next_page:
                    return HttpResponseRedirect(next_page)
                return HttpResponseRedirect('/videos')
            else:
                return HttpResponse('Inactive user')
        else:
            return HttpResponse('invalid login')
    return render(request, 'videos/login.html', {'next': request.GET.get('next', '')})
