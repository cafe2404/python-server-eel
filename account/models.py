from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField



class Account(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email