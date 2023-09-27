from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Dish, Customer, Order
from .forms import CustomerDetailsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from decimal import Decimal

def home(request):
    return render(request, 'customer/home.html')

def menu_view(request):
    # Retrieve all dishes from the Dish model
    dishes = Dish.objects.all()
    
    # Categorize dishes
    starter_dishes = dishes.filter(categories__name='Starter')
    main_course_dishes = dishes.filter(categories__name='Main Course')
    dessert_dishes = dishes.filter(categories__name='Dessert')
    drink_dishes = dishes.filter(categories__name='Drink')
    
    # Retrieve selected dish IDs from the session
    selected_dish_ids = request.session.get('order_details', {}).get('selected_dishes', [])
    
    context = {
        'starter_dishes': starter_dishes,
        'main_course_dishes': main_course_dishes,
        'dessert_dishes': dessert_dishes,
        'drink_dishes': drink_dishes,
        'selected_dish_ids': selected_dish_ids,  # Include selected dish IDs in the context
    }
    
    return render(request, 'customer/menu.html', context)


def dish_detail_view(request, slug):
    dish = get_object_or_404(Dish, slug=slug)
    return render(request, 'customer/dish_detail.html', {'dish': dish})

@login_required
def customer_details_view(request):
    # Check if the user already has customer details
    customer = get_object_or_404(Customer, user=request.user)

    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST, instance=customer)
        if form.is_valid():
            # Update the customer details in the database
            form.save()
            return redirect('menu')  # Redirect to the menu page after saving details
    else:
        form = CustomerDetailsForm(instance=customer)
    
    return render(request, 'customer/customer_details_form.html', {'form': form})

@login_required
def update_selected_dishes(request):
    if request.method == 'POST': # and request.is_ajax()
        # dish_id = request.POST.get('dish_id')
        # is_checked = request.POST.get('is_checked')
        
        # if dish_id and is_checked in ['true', 'false']:
        #     dish_id = int(dish_id)
        #     is_checked = (is_checked == 'true')
            
        #     # Retrieve the selected dishes from the session
        #     selected_dishes = request.session.get('order_details', {}).get('selected_dishes', [])
            
        if is_checked:
            # If the checkbox is checked, add the dish to selected dishes
            if dish_id not in selected_dishes:
                selected_dishes.append(dish_id)
        else:
            # If the checkbox is unchecked, remove the dish from selected dishes
            if dish_id in selected_dishes:
                selected_dishes.remove(dish_id)
        
        # Update the selected dishes in the session
        request.session['order_details']['selected_dishes'] = selected_dishes
        request.session.modified = True  # Mark the session as modified
            
    #         return JsonResponse({'success': True})
    
    # return JsonResponse({'success': False})


@login_required
def delete_selected_dishes(request, dish_id):
    # Retrieve the selected dish IDs from the session
    order_details = request.session.get('order_details', {})
    selected_dish_ids = order_details.get('selected_dishes', [])

    # Check if the dish_id is in the selected_dish_ids list
    if dish_id in selected_dish_ids:
        # Remove the dish_id from the selected_dish_ids
        selected_dish_ids.remove(dish_id)

        # Calculate the updated total price
        updated_total_price = calculate_total_price(selected_dish_ids)

        # Update the selected_dishes and total_price in the session
        order_details['selected_dishes'] = selected_dish_ids
        order_details['total_price'] = updated_total_price
        request.session['order_details'] = order_details
        request.session.modified = True

        return redirect('cart')  # Redirect to the 'cart' page

    
def calculate_total_price(selected_dish_ids):
    # Retrieve the selected dishes and their prices
    selected_dishes = Dish.objects.filter(pk__in=selected_dish_ids)
    
    # Calculate the total price by summing the prices of selected dishes
    total_price = sum(float(selected_dish.price) for selected_dish in selected_dishes)
    
    return total_price

@login_required
def order_view(request):
    if request.method == 'POST':
        selected_dish_ids = request.POST.getlist('selected_dishes')
        
        # if not selected_dish_ids:
        #     # If no dishes are selected, display an error message
        #     return redirect('cart')  # Redirect back to the menu page
        
        # Get the selected dishes
        selected_dishes = Dish.objects.filter(pk__in=selected_dish_ids)
        
        # Calculate total price
        total_price = float(sum(selected_dish.price for selected_dish in selected_dishes))
        
        if request.user.is_authenticated:
            # If the user is authenticated, retrieve their customer details from the database
            try:
                customer = request.user.customer  # one-to-one relationship between User and Customer
            except Customer.DoesNotExist:
                # Handle the case where the customer details don't exist for the user
                return redirect('customer-details')  # Redirect to the customer details view
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
                messages.error(request, "Please provide valid customer details.")
                return redirect('menu')  # Redirect to the menu page
        
        # Store the order details in the session
        request.session['order_details'] = {
            'selected_dishes': [dish.id for dish in selected_dishes],
            'total_price': total_price,
            'customer_id': customer.id,
            'name': customer.name,  # Add name to order details
            'email': customer.email,  # Add email to order details
            'street': customer.street,
            'city': customer.city,
            'state': customer.state,
            'zipcode': customer.zipcode,
        }
        
        # Render the order.html template with order details
        context = {
            'order': request.session['order_details'],  # Pass the order details
            'selected_dishes': selected_dishes,  # Pass the selected dishes
        }
        return render(request, 'customer/order.html', context)
    
    return redirect('menu')

@login_required
def cart_view(request):
    order_details = request.session.get('order_details')
    
    if not order_details or not order_details.get('selected_dishes'):

        if request.user.is_authenticated:
            # If the user is authenticated, retrieve their customer details from the database
            try:
                customer = request.user.customer  # one-to-one relationship between User and Customer
            except Customer.DoesNotExist:
                # Handle the case where the customer details don't exist for the user
                return redirect('customer-details')  # Redirect to the customer details view
            
        request.session['order_details'] = {
        'name': customer.name,
        'email': customer.email,
        'street': customer.street,
        'city': customer.city,
        'state': customer.state,
        'zipcode': customer.zipcode}

        context = {
        'order': request.session['order_details'],  # Pass the order details
        }
        return render(request, 'customer/order.html', context)
    
    # Retrieve selected dishes
    selected_dishes = Dish.objects.filter(pk__in=order_details['selected_dishes'])
    
    email = order_details['email']
    
    order = Order(
        user=request.user,
        name_id=order_details['customer_id'],
        total_price=order_details['total_price'],
        street=order_details['street'],
        city=order_details['city'],
        state=order_details['state'],
        zipcode=order_details['zipcode'],
    )

    order.email = email

    context = {
        'order': order,
        'selected_dishes': selected_dishes,
    }

    return render(request, 'customer/order.html', context)

@login_required
def order_confirmation_view(request):
    # Retrieve the order details from the session
    order_details = request.session.get('order_details')
    
    if not order_details:
        # If order details are not found in the session, redirect to the menu page
        messages.error(request, "No order details found. Please create an order first.")
        return redirect('menu')
    
    # Retrieve selected dishes
    selected_dishes = Dish.objects.filter(pk__in=order_details['selected_dishes'])
    
    # Create an order
    if request.user.is_authenticated:
        order = Order(
            user=request.user,
            name_id=order_details['customer_id'],
            total_price=order_details['total_price'],
            street=order_details['street'],
            city=order_details['city'],
            state=order_details['state'],
            zipcode=order_details['zipcode'],
        )
    else:
        order = Order(
            user=None,  # No authenticated user
            name_id=order_details['customer_id'],
            total_price=order_details['total_price'],
            street=order_details['street'],
            city=order_details['city'],
            state=order_details['state'],
            zipcode=order_details['zipcode'],
        )
    order.save()
    
    # Add selected dishes to the order
    order.items.set(selected_dishes)
    
    # Clear the order details from the session
    request.session.pop('order_details', None)
    
    # Redirect to order-confirmation.html with order details
    context = {
        'order': order,
        'selected_dishes': selected_dishes,
    }
    
    return render(request, 'customer/order_confirmation.html', context)


def contact_us(request):
    if request.method == 'POST':
        sender_name = request.POST.get('name')
        messages.success(request, f'Thank you, {sender_name}! Your message has been sent. We will get back to you soon.', extra_tags='contact_us')

        # Redirect to a thank you page or the same contact page
        return redirect('contact-us')

    return render(request, 'customer/contact_us.html')