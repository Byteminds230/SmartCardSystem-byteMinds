from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Class(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

class CustomUser(AbstractUser):
    # Additional fields
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(unique=True, blank=False, max_length=255)
    password = models.CharField(max_length=255)
    Class = models.ForeignKey(Class, on_delete=models.CASCADE, default=None, blank=True)
    profile = models.ImageField(upload_to='images/profiles/', blank=True, null=True)
    role = models.CharField(
        max_length=50,
        choices=[('Student', 'Student'), ('Admin', 'Admin'), ('Teacher', 'Teacher')],
        default='Student',
        blank=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # Override related_name for groups and user_permissions to avoid conflict
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Custom related_name
        blank=True
    )
