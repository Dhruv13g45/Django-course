from django.shortcuts import render,get_object_or_404
from .models import Products

# Create your views here.
from django.shortcuts import render

def all_products(request):
    all_prods = Products.objects.all()
    return render(request,"website/allProducts.html",{'all_prods' : all_prods})



def singleProduct(request,product_id):
    single_prod = get_object_or_404(Products,pk=product_id)
    return render(request,"website/singleProduct.html",{'single_prod':single_prod})