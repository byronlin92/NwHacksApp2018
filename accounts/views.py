from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


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
            #user = form.save()
            #login(request,user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})