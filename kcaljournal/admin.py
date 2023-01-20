from django.contrib import admin

from .models import Fooditem, Journal, FoodEntry

# Register your models here.
admin.site.register(Fooditem)
admin.site.register(Journal)
admin.site.register(FoodEntry)