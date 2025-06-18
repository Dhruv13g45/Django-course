from django.db import models
from base.BaseProfile import BaseProfile
from django.contrib.auth.models import User

# Create your models here.


class StudentProfile(BaseProfile):
    student = models.OneToOneField(User, on_delete=models.CASCADE,related_name='student_user')
    course = models.ManyToManyField('courses.Course', related_name='student_courses')
    books = models.ForeignKey('library.Book', on_delete=models.SET_NULL, null=True, blank=True, related_name='student_books')
    payment = models.ManyToManyField('payment.Transaction' ,related_name='student_fee_transactions')


class TeacherProfile(BaseProfile):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_user')
    course = models.ManyToManyField('courses.Course', related_name='teacher_courses')
    students = models.ManyToManyField(StudentProfile, related_name ='teacher_teaching_students')



class Librarian(BaseProfile):
    librarian = models.OneToOneField(User, on_delete=models.CASCADE, related_name='librarian_profile')


class FeeManager(BaseProfile):
    fee_manager = models.OneToOneField(User, on_delete=models.CASCADE, related_name='fee_manager_profile')