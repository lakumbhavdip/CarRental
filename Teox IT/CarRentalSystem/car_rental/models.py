from django.utils import timezone
from django.db import models

# Create your models here.
class Admin(models.Model):
    full_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)

class Customer(models.Model):
    full_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(default=timezone.now,null=True)
    updated_at = models.DateTimeField(null=True)
    deleted_at = models.DateTimeField(null=True)    
    is_deleted = models.BooleanField(default=False)
    

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=20, unique=True)
    available = models.BooleanField(default=True)

class CarBooking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now,null=True)
    deleted_at = models.DateTimeField(null=True)
    is_deleted = models.BooleanField(default=False)
    