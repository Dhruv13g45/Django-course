from django.db import models



class BaseProfile(models.Model):
    role_choice = [
        ('STD', "STUDENT"),
        ('TCH', 'TEACHER'),
        ('LIB','LIBRARIAN'),
        ('FM','FEEMANAGER'),
        ('DN','DEAN'),
    ]

    user_name  = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=50)
    user_confirm_password = models.CharField(max_length=50)
    user_role = models.CharField(choices=role_choice)

    class Meta:
        abstract = True