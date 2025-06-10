from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.DecimalField(max_digits=8, decimal_places=0)
    email = models.EmailField(max_length=254, unique=True)  # Ensure email is unique
    password = models.CharField(max_length=100)  # Store hashed passwords in production
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set the field to now every time the object is saved
    is_active = models.BooleanField(default=True)  # Field to indicate if the user is active
    is_admin = models.BooleanField(default=False)  # Field to indicate if the user is an admin
    is_verified = models.BooleanField(default=False)  # Field to indicate if the user is verified
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)  # Optional profile picture field
    bio = models.TextField(null=True, blank=True)  # Optional bio field