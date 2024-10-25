from django.db import models

# Create your models here.
class Book(models.Model):
    tile = models.TextField()
    isbn = models.TextField()
    pubdate = models.DateField()
    mileage = models.IntegerField()
    publisher = models.TextField()
    author = models.TextField()
    description = models.TextField()
    pricesales = models.IntegerField()