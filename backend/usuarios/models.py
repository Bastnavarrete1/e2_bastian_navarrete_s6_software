from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    rol = models.CharField(max_length=20)