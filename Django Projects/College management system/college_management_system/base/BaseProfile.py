from django.db import models
from uuid import uuid4


class BaseProfile(models.Model):
    role_choice = [
        ('STD', 'STUDENT'),
        ('TCH', 'TEACHER'),
        ('DN', 'DEAN'),
        ('LB', 'LIBRARIAN')
    ]
    user_role = models.CharField(choices=role_choice)
    user_name = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='profile_images/')
    user_email = models.EmailField()
    user_phone = models.PositiveBigIntegerField( blank=False, null=False)


    class Meta:
        abstract = True