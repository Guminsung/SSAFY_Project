from django.conf import settings
from django.db import models

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.TextField()

class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(20)