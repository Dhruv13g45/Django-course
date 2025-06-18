from django.shortcuts import render


def welcome_page(request):
    return render(request, 'templates/layout.html')