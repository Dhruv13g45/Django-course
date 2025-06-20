from django.urls import path,include
from . import views

urlpatterns =[
    path('', views.view_all_courses, name='all_courses'),
    path('add_new_course/', views.add_new_course, name='add_new_course'),
    path('delete_course/', views.delete_course, name='delete_course'),
]