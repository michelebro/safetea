from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()