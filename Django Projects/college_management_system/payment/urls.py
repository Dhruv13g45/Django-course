from django.shortcuts import render
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.make_payment, name='make_payment')
]
