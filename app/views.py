from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import NewPostForm, PostScheduleForm
from django.contrib import messages

from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':len(posts)})

#POSTS
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})

def howItWorks(request):
    return render(request, 'howItWorks.html')

def serviceConnections(request):
    return render(request, 'serviceConnections.html')

def meetOurTeam(request):
    return render(request, 'meetOurTeam.html')

def reviews(request):
    return render(request, 'reviews.html')

@login_required
def post_new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.created_at = timezone.now()
            post.updated_at = timezone.now()
            post.save()
            return redirect('posts')
    else:
        form = NewPostForm()
    return render(request, 'post_new.html', {'form': form})


def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    return render(request, 'post_detail.html', {'post': post})

def post_update(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST' and 'Edit_post' in request.POST:
        form = NewPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.updated_at = timezone.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)
    elif request.method == 'POST' and 'Delete_post' in request.POST:
        post.delete()
        return redirect('posts')
    else:
        form = NewPostForm()
    return render(request, 'post_update.html', {'post': post, 'form': form})


def post_schedule(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = PostScheduleForm(request.POST, instance=post)
        if form.is_valid():

            hour_count = form.cleaned_data['hour_count']
            post.total_cost = hour_count * int(post.rate)
            post.scheduled_by = request.user
            post.save()
            messages.info(request, 'You have successfully scheduled this service')
            return redirect('posts')
    else:
        form = PostScheduleForm()
    return render(request, 'post_schedule.html', {'post':post, 'form': form})
