from django.db import models
from django.apps import apps

class Courses(models.Model):
    COURSE_CHOICES = [
        ('CSE', 'Computer Science Engineering'),
        ('ME', 'Mechanical Engineering'),
        ('CE', 'Civil Engineering'),
        ('IT', 'Information Technology'),
        ('AIML', 'Artificial Intelligence and Machine Learning'),
        ('DS', 'Data Science'),
    ]
    course_title = models.CharField(max_length=100, choices=COURSE_CHOICES)
    course_code = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.course_title

    def students(self):
        Student = apps.get_model('students', 'Student')
        return Student.objects.filter(std_course=self)
