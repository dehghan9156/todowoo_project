from django.shortcuts import render,redirect
from .forms import UserSignUpForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,'accounts/home.html')
def signupuser(request):

    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], password=cd['password1'])
            return redirect('accounts:home')
            messages.success(request, 'user register successfuly', 'success')

    else:
        form = UserSignUpForm()
    return render(request, 'accounts/signupuser.html', {'form': form})

def loginuser(request):
    if request.method == 'POST' :
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username = cd['username'],password = cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request, 'user logined successfuly', 'success')
                return redirect('accounts:home')
            else:
                messages.error(request, 'username and password is wrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logoutuser(request):
    logout(request)
    messages.success(request,'User logged out successfully','success')
    return redirect('accounts:home')