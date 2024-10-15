
from django.contrib.auth.models import AbstractUser
from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class CustomUser(AbstractUser):
    # Additional fields can be added here if needed
    name = models.CharField(max_length=255 , blank=False)
    email = models.EmailField(unique=True , blank=False , max_length=255)
    password = models.CharField(max_length=255)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE  , default=None , blank=True)
    profile = models.ImageField(upload_to='images/profiles/', blank=True, null=True)
    role = models.CharField(max_length=50, choices=[('Student', 'Student'), ('admin', 'Admin')], default='Student' , blank=False)
    created_at = models.DateTimeField(auto_now_add=True)