from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class ZASUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)
