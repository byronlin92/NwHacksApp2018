from django.db import models
from django.contrib.auth.models import User
from app.models import Post
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




def get_scheduled_posts(self):
    return Post.objects.filter(scheduled_by=self)

User.add_to_class("get_scheduled_posts",get_scheduled_posts)


