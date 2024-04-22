from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class weather(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class SearchHistory(models.Model):
    user = models.ForeignKey(weather, on_delete=models.CASCADE)  # Replace User with your user model
    city = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now_add=True)
