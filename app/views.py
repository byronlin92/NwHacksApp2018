from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import NewPostForm

def home(request):
    return render(request, 'home.html')

def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})

def post_new(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.created_by = None
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
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.created_by = None
            post.updated_at = timezone.now()
            post.save()
            return redirect('post_detail', {'post':post})
    else:
        form = NewPostForm()
    return render(request, 'post_update.html', {'post': post})
