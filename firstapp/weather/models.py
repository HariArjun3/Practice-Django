from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class weather(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

