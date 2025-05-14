from django.shortcuts import render, get_object_or_404
from .models import Products

# Create your views here.


def products_list(request):
    all_products = Products.objects.all()
    return render(request, "website/home.html",{'all_products' : all_products})

def specific_product(request,product_id):
    single_product = get_object_or_404(Products,pk=product_id)
    return render(request,"website/specific_product.html",{'single_product':single_product})