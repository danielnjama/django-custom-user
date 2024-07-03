from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    phonenumber = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
