from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Category(models.Model):
    customer = models.ForeignKey(Customer, on_delete=SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField()
    createAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description