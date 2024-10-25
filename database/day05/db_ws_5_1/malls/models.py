from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    customer = models.ManyToManyField(Customer)