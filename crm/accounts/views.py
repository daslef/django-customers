from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from .filters import OrderFilter

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

def signup_handle(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def login_handle(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =  request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'accounts/login.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer_orders = customer.order_set.all()
    filter_ = OrderFilter(request.GET, queryset=customer_orders)
    customer_orders = filter_.qs
    context = {
        'customer': customer, 
        'orders': customer_orders, 
        'orders_count': customer_orders.count(),
        'filter_': filter_
        }
    return render(request, 'accounts/customer.html', context)

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(
        Customer, 
        Order, 
        fields=('product', 'status'), 
        extra=5, 
        can_delete=False
        )
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)

    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {
        'formset': formset
    }

    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'formset': form
    }

    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'order': order.product.name
    }
    return render(request, 'accounts/delete_form.html', context)