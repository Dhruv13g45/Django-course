from django.db import models
from uuid import uuid4
# Create your models here.

class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    book_title = models.CharField(max_length=100)
    book_desc = models.TextField(default='')
    book_publisher = models.CharField(max_length=100)
    book_genre = models.CharField(max_length=100)


    def __str__(self):
        return self.book_title