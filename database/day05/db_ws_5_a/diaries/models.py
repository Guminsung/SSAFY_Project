from django.conf import settings
from django.db import models

# Create your models here.
class Diary(models.Model):
    content = models.CharField(max_length=125)
    picture = models.ImageField(blank=True, upload_to='diary/%y/%b/%a')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_diaries')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    content = models.CharField(max_length=125)
    created_at = models.DateTimeField(auto_now_add=True)
