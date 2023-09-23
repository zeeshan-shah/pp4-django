from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('order/', views.order_view, name='order'),
    path('order-confirmation/', views.order_confirmation_view, name='order-confirmation'),
    path('customer-details/', views.customer_details_view, name='customer-details'),
]