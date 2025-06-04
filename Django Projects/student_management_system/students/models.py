from django.db import models
import datetime


class Student(models.Model):
    std_roll = models.AutoField(unique=True,primary_key=True)
    std_name = models.CharField(max_length=100)
    std_email = models.EmailField()
    std_joining_date = models.DateTimeField(default=datetime.datetime.now)
    std_course = models.ManyToManyField('courses.Courses')

    def __str__(self):
        return self.std_name
