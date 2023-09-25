from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu_view, name='menu'),
    path('menu/<slug:slug>/', views.dish_detail_view, name='dish-detail'),
    path('order/', views.order_view, name='order'),
    path('update-selected-dishes/', views.update_selected_dishes, name='update-selected-dishes'),
    path('delete/<int:dish_id>/', views.delete_selected_dishes, name='delete_selected_dishes'),
    path('cart/', views.cart_view, name='cart'),
    path('order-confirmation/', views.order_confirmation_view, name='order-confirmation'),
    path('customer-details/', views.customer_details_view, name='customer-details'),
]