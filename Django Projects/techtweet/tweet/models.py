from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


class TweetModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    tweet_title = models.CharField(max_length=100)
    tweet_message = models.CharField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
       return self.tweet_title


