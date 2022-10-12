from django.urls import path

from . import views

urlpatterns = [
    path('', views.journal, name='journal'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('search/food_register/', views.food_register.as_view(), name='food_register'),
]