from django.http import HttpResponse
from django.shortcuts import render

def layout(request):
    return render(request,"layout.html")

def home(request):
    return render(request,'website/home.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    return render(request,'website/contact.html')
