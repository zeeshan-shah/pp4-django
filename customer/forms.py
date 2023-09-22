# forms.py
from django import forms
from .models import Customer

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'city', 'street', 'state', 'zipcode']  # Include 'email' field
