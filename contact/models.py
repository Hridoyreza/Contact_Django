from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    contactholder = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name