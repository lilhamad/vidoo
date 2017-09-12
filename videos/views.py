# Create your views here.
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Video, Comment, Reply, Watch, Like, Dislike, Heart
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
import json
from django.core.serializers import serialize

class index(ListView):
    template_name = 'videos/index.html'
    context_object_name = 'videos'

    def get_queryset(self):
        return Video.objects.order_by('-view_count').all()


@login_required()
def show(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.user.subscription.value:
        video.view_count = video.view_count+1
        video.save()
        sub = request.user.subscription
        sub.value = sub.value-1
        sub.save()
        Watch(video=video).save()
        is_like = Like.objects.filter(added_by=request.user).filter(video=video)
        is_dislike = Dislike.objects.filter(added_by=request.user).filter(video=video)
        comments = Comment.objects.filter(video=video)
        commentz = []
        for comment in comments:
            hearts = Heart.objects.filter(comment=comment)
            for heart in hearts:
                if heart.added_by_id==request.user.id:
                    commentz.append(comment.id)
        data = comments
        return HttpResponse(data)
    else:
        return HttpResponseRedirect('/accounts/' + str(request.user.id) + '/profile?link=finish&videoid='+str(video.id))


class create(CreateView):
    model = Video
    fields = ['name', 'playlist', 'category', 'path', 'details']


def create_comment(request):
    if request.is_ajax():
        video = Video.objects.get(pk=request.POST['id'])
        if request.method == 'POST':
            comment = Comment(video=video, text=request.POST['text'])
            comment.save()
        comments = Comment.objects.filter(video=video)
        data = serialize('json', comments)
        return HttpResponse(data)
    else:
        video = Video.objects.get(pk=request.POST['id'])
        if request.method == 'POST':
            comment = Comment(video=video, text=request.POST['text'])
            comment.save()
        # return HttpResponseRedirect('/videos/'+str(video.id))


def create_reply(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        reply = Reply(comment=comment, text=request.POST['text'])
        reply.save()
    return HttpResponseRedirect('/videos/'+str(comment.video.id))


def create_like(request, pk):
    video = Video.objects.get(pk=pk)
    if request.method == 'POST':
        like = Like(video=video)
        like.save()
    return HttpResponseRedirect('/videos/'+str(video.id))


def create_dislike(request, pk):
    video = Video.objects.get(pk=pk)
    if request.method == 'POST':
        dislike = Dislike(video=video)
        dislike.save()
    return HttpResponseRedirect('/videos/'+str(video.id))


def create_heart(request, pk):
    comment = Comment.objects.get(pk=pk)
    is_hearted = Heart.objects.filter(comment=comment, added_by=request.user)
    if is_hearted.exists():
        pass
    else:
        if request.method == 'POST':
            heart = Heart(comment=comment)
            heart.save()
    return HttpResponseRedirect('/videos/'+str(comment.video.id))


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