from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Fooditem
# Create your views here.


class SearchView(generic.ListView):
    template_name = 'kcaljournal/search.html'
    context_object_name= 'fooditem_list'

    def get_queryset(self):
        return Fooditem.objects.all()


