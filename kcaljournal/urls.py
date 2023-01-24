from django.urls import path

from . import views


urlpatterns = [
    path('', views.journal, name='journal'),
    path('add_entry/', views.add_entry.as_view(),name='add_entry'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('search/food_register/', views.food_register.as_view(), name='food_register'),
    path('login/', views.login_view, name='login_view'),
    path('login/authenticate/', views.authenticate_view, name='authenticate'),
    path('logout/', views.logout_view, name='logout_view'),
    path('registrate/', views.registrate_view, name='sign_up'),
    path('registrate/process_account/', views.process_account, name='process_account'),
]