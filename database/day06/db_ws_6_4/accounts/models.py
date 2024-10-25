from django.db import models
from django.contrib.auth.models import AbstractUser

from libraries.models import Author

# Create your models here.
class User(AbstractUser):
    subscribtion = models.ManyToManyField(Author, symmetrical=False, related_name='subscriber')