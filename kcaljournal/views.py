from django.shortcuts import render 
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse

from .models import Fooditem
from .forms import FoodForm
# Create your views here.

def journal(request):
    return render(request, "kcaljournal/index.html")

class SearchView(generic.ListView):
    template_name = 'kcaljournal/search.html'
    context_object_name= 'fooditem_list'

    def get_queryset(self):
        return Fooditem.objects.all()

class food_register(generic.CreateView):
    model=Fooditem
    form_class = FoodForm
    template_name= 'kcaljournal/food_form.html'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('search')

    


    

