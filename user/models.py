from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class expenses(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    current_balance=models.DecimalField(max_digits=100,decimal_places=2)
    total_spend=models.DecimalField(max_digits=100,decimal_places=2)
    current_month_spend=models.DecimalField(max_digits=100,decimal_places=2)
    current_month_recieved=models.DecimalField(max_digits=100,decimal_places=2)

class tracker(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date=models.DateField()
    category=models.CharField(max_length=100)
    amount=models.FloatField()
