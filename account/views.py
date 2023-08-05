from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterForm
# Create your views here.
def login_user(request):

    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

        messages.error(request, 'Username Or Password is incorrect')
    
    return render(request, 'account/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = User.objects.create_user(username=username, password=password)
            login(request, user)

            messages.success(request, 'Your account successfully created')
            return redirect('home')

        return render(request, 'account/signup.html', {'form': form})
    
    form = RegisterForm()
    return render(request, 'account/signup.html', {'form': form})
