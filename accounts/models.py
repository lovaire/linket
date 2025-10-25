# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Kita tambahkan field yang kamu mau: display_name
    display_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.username