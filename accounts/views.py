from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login
from .forms import SignUpForm, AccountUpdateForm, UpdatePasswordForm
from django.contrib.auth.models import User
#login decorator
from django.contrib.auth.decorators import login_required




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