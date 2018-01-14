from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login
from .forms import SignUpForm, AccountUpdateForm, UpdatePasswordForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User
from .models import Profile
#login decorator
from django.contrib.auth.decorators import login_required


#ACCOUNTS
def signin(request):
    email = request.POST['emailAddress']
    password = request.POST['password']
    user = authenticate(request, username = email, password = password)
    if user is not None:
        login(request, user)
        render(request, 'posts.html')
    else:
        render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

@login_required
def account_detail(request, user_username):
    user = User.objects.get(username=user_username)
    return render(request, 'account_detail.html', {'user': user})


@login_required
def account_update(request, user_username):
    user = get_object_or_404(User, username=user_username)
    if request.method == 'POST':
        form = AccountUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('account_detail', user_username=user_username)
    else:
        form = AccountUpdateForm()
    return render(request, 'account_update.html', {'user':user, 'form':form})


#PROFILES
def profile_detail(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    return render(request, 'profile_detail.html', {'profile':profile})

@login_required
def profile_update(request, profile_pk):
    profile = get_object_or_404(Profile, pk=profile_pk)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save()
            return redirect('profile_detail', profile_pk=profile_pk)
    else:
        form = ProfileUpdateForm()
    return render(request, 'profile_update.html', {'profile':profile, 'form':form})

@login_required
def password_change(request, user_username):
    user = get_object_or_404(User, username=user_username)
    if request.method == 'POST':
        form = UpdatePasswordForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('account_detail', user_username=user_username)
    else:
        form = UpdatePasswordForm()
    return render(request, 'password_update.html', {'user':user, 'form':form})