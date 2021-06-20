from django.db import models

# Create your models here.

class Flights(models.Model):
    origin = models.CharField(max_length=60)
    destination = models.CharField(max_length=60)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
