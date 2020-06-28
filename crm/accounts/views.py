from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    customers = Customer.objects.all()
    total_customers = customers.count()
    orders = Order.objects.all()
    total_orders = orders.count()
    orders_pending = orders.filter(status='Pending').count()
    orders_delivered = orders.filter(status='Delivered').count()
    context = {
        'orders': orders, 
        'customers': customers, 
        'orders_total': total_orders,
        'orders_pending': orders_pending,
        'orders_delivered': orders_delivered
        }
    
    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer_orders = customer.order_set.all()
    context = {
        'customer': customer, 
        'orders': customer_orders, 
        'orders_count': customer_orders.count()
        }
    return render(request, 'accounts/customer.html', context)
