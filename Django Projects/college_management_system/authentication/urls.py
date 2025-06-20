from django.shortcuts import render
from django.urls import path,include
form . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
]