
from django.urls import path
from . import views

urlpatterns = [
    path('',views.show_all_tweet,name='show_all_tweet'),
    path('create_tweet/',views.create_new_tweet, name='create_new_tweet'),
    path('edit_tweet/<int:tweetid>/',views.edit_tweet, name='edit_tweet'),
    path('delete_tweet/<int:tweetid>/',views.delete_tweet, name='delete_tweet'),
    path('register/', views.display_registor_route, name='register'),
    path('login/', views.display_login_route,name='login'),
    path('logout/', views.display_logout_route,name='logout'),
]
