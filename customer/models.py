from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class MealCategory(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    image = CloudinaryField('image')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ForeignKey(MealCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
