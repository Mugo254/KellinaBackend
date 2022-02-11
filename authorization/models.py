from django.db import models
from django.contrib.auth.models import AbstractUser,Group

# Create your models here.
class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['groups_id']