from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('service_provider', 'Service Provider'),
    )

    email = models.EmailField(unique=True)   
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=15, unique=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username