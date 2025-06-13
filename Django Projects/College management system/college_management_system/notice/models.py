from django.utils import timezone
from django.db import models

# Create your models here.


class Notice(models.Model):
    notice_title = models.CharField(max_length=100)
    notice_desc = models.TextField(default='This is a Notice')
    notice_issued_at = models.DateTimeField(default=timezone.now)