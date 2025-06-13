
from django.db import models
from college_management_system.base.BaseProfile import BaseProfile
from academics.models import Courses
from library.models import Book
from django.contrib.auth.models import User

# Create your models here.
class StudentProfile(BaseProfile):
    student_user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='students')
    student_enrolled_course = models.ForeignKey(Courses, on_delete=models.SET_NULL, related_name='student_courses')
    std_books = models.ManyToManyField(Book, related_name='student_issued_books')
    
class TeacherProfile(BaseProfile):
    teacher_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teachers')
    teacher_enrolled_courses = models.ManyToManyField(Courses, related_name='teacher_courses')


class Librarian(BaseProfile):
    lib_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='librarian')