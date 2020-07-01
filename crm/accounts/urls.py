from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_handle, name='signup'),
    path('login/', views.login_handle, name='login'),
    path('logout/', views.logout_handle, name='logout'),
    path('user/', views.userProfile, name='user-profile'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/<str:pk>', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order'),
]
