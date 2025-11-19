from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.

class Customuser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(null=True)
