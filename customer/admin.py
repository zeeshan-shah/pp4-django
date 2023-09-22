from django.contrib import admin
from .models import Customer, Dish, MealCategory, Order

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'city', 'state')

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):

    list_display = ('name', 'categories', 'price')

admin.site.register(MealCategory)