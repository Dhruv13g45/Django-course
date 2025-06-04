from django.db import models
from students.models import Student
from courses.models import Courses

# Create your models here.


class Grades(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    score = models.FloatField()
