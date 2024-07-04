from django.db import models
# from . views import get_activation_code
from .utils import get_activation_code

# Create your models here.

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=15)
    activation_code = models.PositiveIntegerField(default=get_activation_code())
    account_active = models.BooleanField(default=False)
