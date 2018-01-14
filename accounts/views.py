from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.models import User

#login decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



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