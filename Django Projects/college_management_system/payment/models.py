from uuid import uuid4
from django.db import models
from django.utils import timezone

# Create your models here.
class Transaction(models.Model):
    transaction_id = models.UUIDField(primary_key=True, default=uuid4)
    transaction_message = models.CharField(max_length=100)
    course = models.ForeignKey('courses.Course', on_delete=models.SET_NULL, null=True, blank=True,related_name='course_payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    student = models.ForeignKey('users.StudentProfile', on_delete=models.CASCADE, related_name='transaction_specific_student')
    transaction_date_time = models.DateTimeField(default=timezone.now)
    transaction_status = models.CharField(max_length =100,choices= [('failed','failed'),('success','success')])


class FeeStructure(models.Model):
    course = models.OneToOneField('courses.Course', on_delete=models.CASCADE, related_name='course_fee_structure')
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
