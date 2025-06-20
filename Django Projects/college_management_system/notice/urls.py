from django.urls import path,include
from django.shortcuts import render
from . import views

urlpatterns = [
    path("", views.view_all_notices,name='view_all_noitces'),
    path("add_notice/", views.add_notice,name='add_new_noitce'),
    path("view_notice/<int: notice_id>", views.view_notice,name='view_noitce'),
]