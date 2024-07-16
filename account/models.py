from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


class Account(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    