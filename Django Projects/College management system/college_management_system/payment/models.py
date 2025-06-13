from django.db import models
from uuid import uuid4
from django.utils import timezone

from college_management_system.academics.models import Course
from college_management_system.users.models import StudentProfile
# Create your models here.

class Transaction_model(models.Model):
    transaction_id = models.UUIDField(primary_key=True,unique=uuid4)
    transaction_date = models.DatTimeField(default=timezone.now)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='student_transactions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_transactions')
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_desc = models.CharField(max_length=400)
    transacton_status = models.CharField(max_length=20, default='SUCCESS')
