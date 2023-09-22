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

def order_view(request):
    if request.method == 'POST':
        selected_dish_ids = request.POST.getlist('selected_dishes')
        
        # Get the selected dishes
        selected_dishes = Dish.objects.filter(pk__in=selected_dish_ids)
        
        # Calculate total price
        total_price = sum(selected_dish.price for selected_dish in selected_dishes)
        
        if request.user.is_authenticated:
            # If the user is authenticated, retrieve their customer details from the database
            try:
                customer = request.user.customer  # Assuming you have a one-to-one relationship between User and Customer
            except Customer.DoesNotExist:
                # Handle the case where the customer details don't exist for the user
                return redirect('menu')  # Redirect to the menu page
                
        else:
            # If the user is not authenticated, process the form data to create a new customer
            form = CustomerDetailsForm(request.POST)
            if form.is_valid():
                # Create a new customer instance with the form data
                customer = form.save(commit=False)
                customer.user = request.user  # Associate the customer with the current user
                customer.save()

            else:
                # Handle the case where the form data is invalid
                return redirect('menu')  # Redirect to the menu page
        
        # Create an order
        order = Order(
            user=request.user,
            name=customer,
            total_price=total_price,
            street=customer.street,
            city=customer.city,
            state=customer.state,
            zipcode=customer.zipcode,
        )
        order.save()
        
        # Add selected dishes to the order
        order.items.set(selected_dishes)
        
        # Redirect to order.html with order details
        context = {
            'order': order,
            'selected_dishes': selected_dishes,
        }
        return render(request, 'customer/order.html', context)
    
    return redirect('menu')