from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse



# Create your views here.


def login_view(request):
    return render(request, "accounts/registration/login.html")


def authenticate_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('')
    else:
        #incorrect login_details
        print("user not logged in")
        pass
