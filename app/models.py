from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    price = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, unique=True)
    message = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    # starter = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

