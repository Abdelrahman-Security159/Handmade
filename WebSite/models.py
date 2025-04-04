from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    ROLE_CHOICES = [
        ('user', 'USER'),
        ('owner', 'OWNER'),
    ]
        
    first_name = models.CharField(max_length=32, blank=True, null=True)
    middle_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=32, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)

    phone = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=16, choices=ROLE_CHOICES, default="user")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    
class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=1024, blank=True, null=True)
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='owned_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class Shop(models.Model):
    name = models.CharField(max_length=32)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='owned_shops')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='purchased_shops')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name