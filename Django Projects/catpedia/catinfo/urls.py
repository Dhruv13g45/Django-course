from django.urls import path
from .  import views
urlpatterns = [
    path('', views.all_cats_fetch ,name="main view"),
    path('<int:catid>/', views.individual_cat,name='individual_cat')
]
