import random

from django.contrib.auth.models import AbstractUser

from django.db import models

# Create your models here.

class Customuser(AbstractUser):
    phone=models.IntegerField(null=True)
    role=models.CharField(null=True)
    otp = models.CharField(null=True)
    is_verified = models.BooleanField(default=False)


    def generate_otp(self):
        otp=str(random.randint(1000,9999))+str(self.id)
        self.otp=otp
        self.save()

