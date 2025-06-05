import datetime
from django.db import models
from django.apps import apps

class Courses(models.Model):
    course_title = models.CharField(max_length=100)
    course_code = models.AutoField(primary_key=True)
    course_desc = models.TextField(default='')

    def __str__(self):
        return self.course_title

    def students(self):
        Student = apps.get_model('students', 'Student')
        return Student.objects.filter(std_course=self)
