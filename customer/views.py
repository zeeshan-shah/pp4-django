from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Dish, Customer, Order
from .forms import CustomerDetailsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from decimal import Decimal


def home(request):
    """
    Render the home page.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'customer/home.html')


def menu_view(request):
    """
    Render the menu page with categorized dishes.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: The rendered menu page with categorized dishes.
    """
    # Retrieve all dishes from the Dish model
    dishes = Dish.objects.all()

    # Categorize dishes
    starter_dishes = dishes.filter(categories__name='Starter')
    main_course_dishes = dishes.filter(categories__name='Main Course')
    dessert_dishes = dishes.filter(categories__name='Dessert')
    drink_dishes = dishes.filter(categories__name='Drink')

    # Retrieve selected dish IDs from the session
    selected_dish_ids = request.session.get(
        'order_details', {}).get('selected_dishes', [])

    context = {
        'starter_dishes': starter_dishes,
        'main_course_dishes': main_course_dishes,
        'dessert_dishes': dessert_dishes,
        'drink_dishes': drink_dishes,
        # Include selected dish IDs in the context
        'selected_dish_ids': selected_dish_ids,
    }

    return render(request, 'customer/menu.html', context)


def dish_detail_view(request, slug):
    """
    Render the detail view of a specific dish.

    Args:
        request: The HTTP request.
        slug (str): The slug of the dish.

    Returns:
        HttpResponse: The rendered dish detail page.
    """
    dish = get_object_or_404(Dish, slug=slug)
    return render(request, 'customer/dish_detail.html', {'dish': dish})


@login_required
def customer_details_view(request):
    """
    Render the customer details form.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: The rendered customer details form page.
    """
    # # Check if the user already has a customer profile
    customer, create = Customer.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST, instance=customer)
        if form.is_valid():
            # Update the customer details in the database
            form.save()
            # Redirect to the menu page after saving details
            return redirect('menu')
    else:
        form = CustomerDetailsForm(instance=customer)

    return render(request,
                  'customer/customer_details_form.html', {'form': form})


@login_required
def delete_selected_dishes(request, dish_id):
    """
    Delete a selected dish from the cart.

    Args:
        request: The HTTP request.
        dish_id (int): The ID of the dish to be removed.

    Returns:
        HttpResponseRedirect: Redirects to the cart page
        after removing the dish.
    """
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
    """
    Calculate the total price of selected dishes.

    Args:
        selected_dish_ids (list): List of selected dish IDs.

    Returns:
        float: The total price of the selected dishes.
    """
    # Retrieve the selected dishes and their prices
    selected_dishes = Dish.objects.filter(pk__in=selected_dish_ids)
    # Calculate the total price by summing the prices of selected dishes
    total_price = sum(float(selected_dish.price)
                      for selected_dish in selected_dishes)

    return total_price


@login_required
def order_view(request):
    """
    Handle the ordering of selected dishes.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: The rendered order.html page.
    """
    if request.method == 'POST':
        selected_dish_ids = request.POST.getlist('selected_dishes')

        # Get the selected dishes
        selected_dishes = Dish.objects.filter(pk__in=selected_dish_ids)

        # Calculate total price
        total_price = float(
            sum(selected_dish.price for selected_dish in selected_dishes))

        if request.user.is_authenticated:
            # If the user is authenticated, retrieve their customer details
            # from the database
            try:
                # one-to-one relationship between User and Customer
                customer = request.user.customer
            except Customer.DoesNotExist:
                # Handle the case where the customer details don't exist
                # for the user
                # Redirect to the customer details view
                return redirect('customer-details')
        else:
            # If the user is not authenticated, process the form data to
            # create a new customer
            form = CustomerDetailsForm(request.POST)
            if form.is_valid():
                # Create a new customer instance with the form data
                customer = form.save(commit=False)
                customer.user = request.user
                # Associate the customer with the current user
                customer.save()
            else:
                # Handle the case where the form data is invalid
                messages.error(
                    request, "Please provide valid customer details.")
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
            # Pass the order details
            'order': request.session['order_details'],
            'selected_dishes': selected_dishes,  # Pass the selected dishes
        }
        return render(request, 'customer/order.html', context)

    return redirect('menu')


@login_required
def cart_view(request):
    """
    Render the cart view with selected dishes.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: The rendered cart view page.
    """
    order_details = request.session.get('order_details')

    if not order_details or not order_details.get('selected_dishes'):

        if request.user.is_authenticated:
            # If the user is authenticated, retrieve their customer details
            # from the database
            try:
                # one-to-one relationship between User and Customer
                customer = request.user.customer
            except Customer.DoesNotExist:
                # Handle the case where the customer details don't exist
                # for the user
                # Redirect to the customer details view
                return redirect('customer-details')

        request.session['order_details'] = {
            'name': customer.name,
            'email': customer.email,
            'street': customer.street,
            'city': customer.city,
            'state': customer.state,
            'zipcode': customer.zipcode}

        context = {
            # Pass the order details
            'order': request.session['order_details'],
        }
        return render(request, 'customer/order.html', context)

    # Retrieve selected dishes
    selected_dishes = Dish.objects.filter(
        pk__in=order_details['selected_dishes'])

    order = Order(
        user=request.user,
        name_id=order_details['customer_id'],
        email=order_details['email'],
        total_price=order_details['total_price'],
        street=order_details['street'],
        city=order_details['city'],
        state=order_details['state'],
        zipcode=order_details['zipcode'],
    )

    context = {
        'order': order,
        'selected_dishes': selected_dishes,
    }

    return render(request, 'customer/order.html', context)


@login_required
def order_confirmation_view(request):
    """
    Render the order confirmation view with order details.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: The rendered order confirmation view page.
    """
    # Retrieve the order details from the session
    order_details = request.session.get('order_details')

    if not order_details:
        # If order details are not found in the session, redirect
        # to the menu page
        messages.error(
            request, "No order details found. Please create an order first.")
        return redirect('menu')

    # Retrieve selected dishes
    selected_dishes = Dish.objects.filter(
        pk__in=order_details['selected_dishes'])

    # Check if any of the required customer details are missing
    if not (order_details['name'] and order_details['email'] and
            order_details['street'] and order_details['city'] and
            order_details['state'] and order_details['zipcode']):
        messages.error(
            request, "Please fill out all customer details "
            "before confirming the order.")
        return redirect('customer-details')

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

    # Render the order-confirmation.html template with order details
    context = {
        'order': order,
        'selected_dishes': selected_dishes,
    }

    return render(request, 'customer/order_confirmation.html', context)


def contact_us(request):
    """
    Handle contact form submissions.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: The rendered contact form or a thank you page.
    """
    if request.method == 'POST':
        sender_name = request.POST.get('name')
        messages.success(
            request,
            f'Thank you, {sender_name}! Your message has been sent. '
            'We will get back to you soon.',
            extra_tags='contact_us'
        )

        # Redirect to a thank you page or the same contact page
        return redirect('contact-us')

    return render(request, 'customer/contact_us.html')


@login_required
def customer_profile(request):
    """
    Render the customer profile view.

    Args:
        request: The HTTP request.

    Returns:
        HttpResponse: The rendered customer profile view page.
    """
    # Check if the user already has customer details
    customer = get_object_or_404(Customer, user=request.user)
    if request.method == 'POST':
        return redirect('customer-details')
    else:
        context = {
            'name': customer.name,  # Add name to order details
            'email': customer.email,  # Add email to order details
            'street': customer.street,
            'city': customer.city,
            'state': customer.state,
            'zipcode': customer.zipcode,
        }

        return render(request, 'customer/customer_profile.html', context)
