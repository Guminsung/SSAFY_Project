# articles/models.py
from django.conf import settings
from django.db import models


class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_users')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)