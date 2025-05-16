from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='products/')
    product_price = models.IntegerField()
    product_desc = models.TextField(default='')


    def __str__(self):
        return self.product_name