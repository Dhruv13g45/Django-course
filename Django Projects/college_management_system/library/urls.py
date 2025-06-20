from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.view_all_books, name='view_all_books'),
    path('add_new_book/', views.add_new_book, name='add_new_book'),
    path('assign_new_book', views.assign_new_book, name='assign_new_book'),
    path('delete_book/<int: book_id>', views.delete_book, name='delete_book'),
]