from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=200, null=True, blank=True)
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)