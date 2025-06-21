from uuid import uuid4
from django.utils import timezone
from django.db import models

# Create your models here.

class Course(models.Model):
    course_choice = [
        ('CSE','Computer Science'),
        ('ECE','Electrical'),
        ('IT','Information Technology'),
        ('ME','Mechanical'),
        ('AI/ML','Artifical Intelligence and Machine Learning'),
        ('DS','Data Science'),
    ]
    course_id = models.UUIDField(default=uuid4, primary_key=True)
    course_name = models.CharField(max_length = 100 ,choices=course_choice)
    course_start_date = models.DateTimeField(default=timezone.now)
    course_end_date = models.DateTimeField(default=timezone.now)
    course_fees = models.DecimalField(max_digits=10, decimal_places=2)
    course_intake = models.IntegerField()

    def __str__(self):
        return self.course_name