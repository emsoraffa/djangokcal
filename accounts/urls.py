from django.urls import path

from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login_view'),
    path('accounts/login/authenticate/', views.authenticate, name='authenticate'),
 ]
