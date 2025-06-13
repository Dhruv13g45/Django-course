from django.db import models


# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)
    book_desc = models.TextField(default='No Description')
    book_pages = models.IntegerField()
    book_genre = models.CharField(max_length=100)