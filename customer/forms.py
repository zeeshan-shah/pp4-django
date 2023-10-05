from django import forms
from .models import Customer


class CustomerDetailsForm(forms.ModelForm):
    """
    Form for editing customer details.

    This form allows users to edit their customer details,
    including name, email, city, street, state, and zipcode.

    Attributes:
        name (str): The name of the customer.
        email (str): The email address of the customer.
        city (str): The city where the customer resides.
        street (str): The street address of the customer.
        state (str): The state where the customer resides.
        zipcode (str): The postal code of the customer's location.

    Meta:
        model (Customer): The Customer model used for creating the form.
        fields (list): The list of fields to include in the form.

    """
    class Meta:
        model = Customer
        fields = ['name', 'email', 'city', 'street', 'state', 'zipcode']
