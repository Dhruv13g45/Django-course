from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.products_list,name='all_products'),
    path("<int:product_id>/", views.specific_product, name='specific_product'),

]
