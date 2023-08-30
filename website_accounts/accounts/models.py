from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.


class CustomerUser(AbstractUser):
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = 'phone_number' #login with phone number
    REQUIRED_FIELDS = ['username']               ##while creating super user asking information
                                