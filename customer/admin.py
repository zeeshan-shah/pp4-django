from django.contrib import admin
from .models import Customer, Dish, MealCategory, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Customer model.

    This configuration specifies how the Customer model is displayed in the
    Django admin interface.

    Attributes:
        list_display (tuple): Fields to display in the list view.

    """
    list_display = ('name', 'email', 'city', 'state')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Dish model.

    This configuration specifies how the Dish model is displayed in the
    Django admin interface.

    Attributes:
        prepopulated_fields (dict): Fields to generate from other fields.
        list_display (tuple): Fields to display in the list view.

    """
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'categories', 'price')


admin.site.register(MealCategory)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Order model.

    This configuration specifies how the Order model is displayed in the
    Django admin interface.

    Attributes:
        list_display (tuple): Fields to display in the list view.

    """
    list_display = ('created_at', 'name', 'total_price', 'city')
