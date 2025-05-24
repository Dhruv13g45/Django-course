from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.



def all_cats_fetch(request):
    url = "https://api.freeapi.app/api/v1/public/cats"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)    
    all_cats = response.json()
    return render(request,'index.html', {'all_cats' : all_cats})


def individual_cat(request,catid): 
    url = f"https://api.freeapi.app/api/v1/public/cats/{catid}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)    
    single_cat = response.json()
    return render(request,'individual.html',{'single_cat':single_cat})