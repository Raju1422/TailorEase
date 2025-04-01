from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ServiceProvider(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="service_provider_profile")
    shop_name = models.CharField(max_length=100)
    experience = models.IntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.shop_name} ({self.opening_time} - {self.closing_time})"