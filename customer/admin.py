from django.contrib import admin
from .models import Customer, Dish, MealCategory, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'city', 'state')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'categories', 'price')


admin.site.register(MealCategory)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = ('created_at', 'name', 'total_price', 'city')
