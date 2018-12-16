from django.db import models
from django.contrib import admin

# Create your models here.
class Post(models.Model):
    pass
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=40)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

admin.site.register(Post)
