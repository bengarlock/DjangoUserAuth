from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    name = models.CharField(default='', max_length=100)
    owner = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField

