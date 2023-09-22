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

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Dish)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Fetch street, city, state, and zipcode from the related Customer instance
    street = models.CharField(max_length=100, editable=False)
    city = models.CharField(max_length=100, editable=False)
    state = models.CharField(max_length=100, editable=False)
    zipcode = models.CharField(max_length=10, editable=False)

    def save(self, *args, **kwargs):
        # Fetch street, city, state, and zipcode from the related Customer instance
        self.street = self.name.street
        self.city = self.name.city
        self.state = self.name.state
        self.zipcode = self.name.zipcode
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} by {self.name}"
