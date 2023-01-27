from datetime import date
from django.shortcuts import render, redirect 
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from .models import Fooditem, Journal, FoodEntry
from .forms import FoodForm, FoodEntryForm

# Create your views here.
TODAY = str(date.today().strftime('%Y-%m-%d'))

@login_required
def journal(request):
    user_diary = Journal.objects.get(user=request.user)
    
    day_selected = request.GET.get('day_selected', TODAY)
    food_entries = list(user_diary.get_food(date=day_selected))
    nutritional_values = FoodEntry.list_food(food_entries)

    context = {
        'user':request.user.is_authenticated,
        'username':request.user.username,
        'food':food_entries,
        'nutritional_values':nutritional_values,
        'totals':user_diary.calculate_nutrition(TODAY),
        'day_selected':day_selected,
        'date_created':user_diary.get_date_created(),
    }
    return render(request, "kcaljournal/index.html", context)

class add_entry(LoginRequiredMixin ,generic.CreateView):
    #need to find a way to access request.user withing CreateView
    model=FoodEntry
    form_class = FoodEntryForm
    template_name= 'kcaljournal/add_entry_form.html'


    def form_valid(self, form):
        self.entry = form.save(commit=False)
        self.entry.journal = Journal.objects.get(user=self.request.user)
        self.entry.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('journal')

    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user'] = self.request.user.is_authenticated
        return context


class FoodDetail(LoginRequiredMixin, generic.DetailView):
    template_name = 'kcaljournal/details.html'
    model = Fooditem


class SearchView(generic.ListView):
    template_name = 'kcaljournal/search.html'
    context_object_name= 'fooditem_list'
    paginate_by= 1
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
    return render(request, "registration/login.html", {"user":False})


def authenticate_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('journal'))
    else:
        #incorrect login_details
        return render(request, "registration/login.html", {"user":False, "message":"Your login information was incorrect."})
    

def logout_view(request):
    logout(request)
    return redirect(reverse('login_view'))



def registrate_view(request):
    return render(request, "registration/registrate.html", {"user":False})


def process_account(request):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']

    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password)
    user_jornal = Journal(user=user, date_created=TODAY)
    user_jornal.save()
    login(request, user)
    
    return redirect(reverse('journal'))


