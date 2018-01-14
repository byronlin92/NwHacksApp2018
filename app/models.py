from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # starter = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
