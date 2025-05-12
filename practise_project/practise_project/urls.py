
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.layout, name='common layout'),
    path('home/',views.home,name='home route'),
    path('about/',views.about,name='about route'),
    path('contact/',views.contact,name='contact route')
]
