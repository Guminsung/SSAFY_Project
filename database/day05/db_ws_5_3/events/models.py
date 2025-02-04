from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    participant = models.ManyToManyField("Participant", related_name='events')
    date = models.DateField()
    location = models.TextField()

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name