from django.shortcuts import render, redirect
from django.views import generic
from .models import Dish, Customer, Order
from .forms import CustomerDetailsForm


def home(request):
    return render(request, 'customer/base.html')

def menu_view(request):
    # Retrieve all dishes from the Dish model
    dishes = Dish.objects.all()
    
    # Categorize dishes
    starter_dishes = dishes.filter(categories__name='Starter')
    main_course_dishes = dishes.filter(categories__name='Main Course')
    dessert_dishes = dishes.filter(categories__name='Dessert')
    drink_dishes = dishes.filter(categories__name='Drink')
    
    context = {
        'starter_dishes': starter_dishes,
        'main_course_dishes': main_course_dishes,
        'dessert_dishes': dessert_dishes,
        'drink_dishes': drink_dishes,
    }
    
    return render(request, 'customer/menu.html', context)

def customer_details_view(request):
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST)
        if form.is_valid():
            # Save the customer details to the database
            customer = form.save(commit=False)
            customer.user = request.user
            customer.save()
            return redirect('menu')  # Redirect to the menu page after saving details
    else:
        form = CustomerDetailsForm()
    
    return render(request, 'customer/customer_details_form.html', {'form': form})