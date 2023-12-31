from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterForm, UserEditForm, UserEdit, DivErrorList
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


# With forms.Form
def user_edit(request):

    name = request.user.first_name
    last = request.user.last_name
    email = request.user.email
    form = UserEditForm(initial={'first_name':name, "last_name":last, 'email':email})
    
    if request.method == "POST":
        form = UserEditForm(data=request.POST, initial={'first_name':name, "last_name":last, 'email':email})
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.filter(username=request.user).update(first_name=cd['first_name'],last_name=cd['last_name'], email=cd['email'])


    return render(request, 'account/edit.html',{'form': form} )



# With forms.ModelForm
def user_edit_model(request):
    form = UserEdit(instance=request.user)

    if request.method == "POST":
        form = UserEdit(instance=request.user, data=request.POST, error_class= DivErrorList)
        if form.is_valid():
            form.save()

    return render(request, 'account/edit.html', {'form': form})