from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Fooditem
from .forms import FoodForm
# Create your views here.

@login_required
def journal(request):
    context = {
        'user':request.user.is_authenticated,
        'username':request.user.username
    }
    return render(request, "kcaljournal/index.html", context)


class SearchView(LoginRequiredMixin ,generic.ListView):
    template_name = 'kcaljournal/search.html'
    context_object_name= 'fooditem_list'
    def get_queryset(self):
        return Fooditem.objects.all()
    
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user'] = self.request.user.is_authenticated
        return context


class food_register(LoginRequiredMixin ,generic.CreateView):
    model=Fooditem
    form_class = FoodForm
    template_name= 'kcaljournal/food_form.html'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('search')
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user'] = self.request.user.is_authenticated
        return context

    

def login_view(request):
    return render(request, "registration/login.html")


def authenticate_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('journal'))
    else:
        #incorrect login_details
        print("user not logged in")
        pass
    

def logout_view(request):
    logout(request)
    return redirect(reverse('login_view'))
