from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse



# Create your views here.


def login_view(request):
    return render(request, "accounts/registration/login.html")


def authenticate_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, reverse(viewname='journal'))
    else:
        #incorrect login_details
        print("user not logged in")
        pass
