from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Feature for future autentication.
    pass

# Model for products sold.
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=24, null=False)
    description = models.CharField(max_length=280, blank=True, null=True)
    picture = models.ImageField(upload_to='product_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__ (self):
    return f"{self.product_id} {self.name}"

# Model for contact us form.
class Contact_Form(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    # Using max lenght of 17 in case customer enters area code, country code or dashes.
    phone = models.CharField(max_length=17)
    message = models.TextField(max_length=264, blank=True)

def __str__ (self):
    return f"{self.first_name} {self.last_name} - {self.phone}"
