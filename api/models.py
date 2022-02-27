from django.db import models
from django.contrib.auth.models import AbstractUser,Group
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token


# Create your models here.
class Items(models.Model):
    
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    unit_price = models.IntegerField() 
       
class Receipt(models.Model):
    name = models.CharField(max_length=30)
    items = models.ForeignKey(Items, on_delete = models.SET_NULL, null=True)
    
    @property
    def total_price(self):
        total_item_price = self.items.quantity * self.items.unit_price
        return total_item_price

class User(AbstractUser):
    groups = models.ForeignKey(Group, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    phonenumber = models.IntegerField(null=True)
    username = None
    receipt = models.ForeignKey(Receipt, on_delete=models.SET_NULL, null=True)
    item = models.ForeignKey(Items,on_delete=models.SET_NULL, null = True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['groups_id']
    

    
    

#Generate Auth Token when Registering and storing the value in the database.
# @receiver(post_save, sender= settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance = None, created = False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
