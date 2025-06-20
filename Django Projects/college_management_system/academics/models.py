from django.db import models

# Create your models here.

class Result(models.Model):
    students = models.ForeignKey('users.StudentProfile', on_delete=models.CASCADE, related_name='student_results')
    course = models.OneToOneField('courses.Course',on_delete=models.SET_NULL,null=True, blank=True,related_name='course_result')
    grade = models.CharField(max_length=100,choices=[('A+', 'Excellent'),('A', 'Great'),('B','Better'), ('C', 'Good'), ('D', 'Fail')])