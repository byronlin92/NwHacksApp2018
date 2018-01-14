from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    rate = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, unique=True)
    message = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

    #for scheduling
    scheduled_by = models.ForeignKey(User, related_name='posts_scheduled_by', on_delete=models.CASCADE, null=True)
    total_cost = models.IntegerField(null=True)
