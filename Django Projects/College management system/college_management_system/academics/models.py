from django.db import models
from uuid import uuid4
from django.utils import timezone
from django.db.models import UniqueConstraint
from college_management_system.users.models import StudentProfile, TeacherProfile

# Create your models here.




class Course(models.Model):
    is_active = models.BooleanField(default=True)
    course_id = models.UUIDField(primary_key=True, default=uuid4)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField(default='')
    course_start_date = models.DateTimeField(default=timezone.now)
    course_end_date = models.DateTimeField()


class Attendence(models.Model):
    attendence_options = [
        ('Pr', 'Present'),
        ('Ab', 'Absent'),
        ('Nr', 'Not Recorded'),
    ]
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='student_attendences')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_attendences')
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True, related_name='attende_teacher')
    attendence_date = models.DateTimeField(default=timezone.now)
    attendence_status = models.CharField(choices=attendence_options)

    class Meta:
         constraints = [
            UniqueConstraint(fields=['student', 'course', 'attendence_date'], name='unique_student_course_attendenceDate'),
        ]



class Result(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.SET_NULL, null=True, related_name='student_results')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='course_reaults')
    result_total_marks = models.IntegerField()
    result_obtained_marks = models.IntegerField()
    result_total_percentage = models.FloatField()