from django.contrib import admin
from .models import Customer, Dish, MealCategory, Order

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'city', 'state')
