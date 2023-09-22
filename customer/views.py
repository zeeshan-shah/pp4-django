from django.shortcuts import render, redirect
from django.views import generic
from .models import Dish, Customer, Order
from .forms import CustomerDetailsForm


def home(request):
    return render(request, 'customer/base.html')