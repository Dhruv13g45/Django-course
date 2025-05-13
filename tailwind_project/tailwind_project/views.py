from django.shortcuts import render


def temp_view(request):
    return render(request,"layout.html")

def home_view(request):
    return render(request,"website/home.html")