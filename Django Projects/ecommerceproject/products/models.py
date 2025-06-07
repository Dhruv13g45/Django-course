from django.db import models
from base.models import BaseModel


# Create your models here.


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category_image')
    slug = models.SlugField(unique=True, null=True, blank = True)




class Products(BaseModel):
    product_name = models.CharField(max_length=100)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products category')
    product_price = models.IntegerField()
    slug = models.SlugField(unique=True)
    product_desc = models.TextField(default='')




class ProductImage(BaseModel):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,related_name='products image')
    product_image = models.ImageField(upload_to='product_image')