from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    
    path('signup/', views.signup_handle, name='signup'),
    path('login/', views.login_handle, name='login'),
    path('logout/', views.logout_handle, name='logout'),
    
    path('user/', views.userProfile, name='user-profile'),
    path('settings/', views.userSettings, name='user-settings'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    
    path('create_order/<str:pk>', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order'),
    
    path(
        'reset_password', 
        auth_views.PasswordResetView.as_view(),
        name='reset_password'
        ),

    path(
        'reset_password_sent', 
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),

    path(
        'reset_password/<uidb64>/<token>', 
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),

    path(
        'reset_password_complete', 
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
        )

]
