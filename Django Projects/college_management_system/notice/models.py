from django.utils import timezone
from uuid import uuid4
from django.db import models

# Create your models here.
class Notice(models.Model):
    notice_id = models.UUIDField(primary_key=True, default=uuid4)
    notice_title = models.CharField(max_length=100)
    noitce_message = models.TextField(default='')
    notice_created_at = models.DateTimeField(default=timezone.now)