from django.db import models
from students.models import Student
from courses.models import Courses

# Create your models here.

class Attendence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    attendence_date = models.DateField()
    attendence_status = models.CharField(max_length=100, choices=[('Present','Present'),('Absent','Absent')])