from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    work = models.CharField(max_length=100)
    content = models.TextField()
    recommends = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='recommended_todos')
    is_completed = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)