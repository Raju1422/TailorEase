from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class ServiceProvider(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE,related_name="customer_profile")
    address = models.TextField()

    def __str__(self):
        return self.user.username
