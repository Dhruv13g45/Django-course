from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.all_products,name='all products url'),
    path("<int:product_id>/", views.singleProduct,name='singleProduct')
]
