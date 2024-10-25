from django.db import models

# Create your models here.
class Diary(models.Model):
    content = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)