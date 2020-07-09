from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'py-1 px-1 text-gray-900 outline-none block h-full w-full',
                'autocomplete': 'false',
                'placeholder': 'enter new username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'py-1 px-1 outline-none block h-full w-full',
                'autocomplete': 'false'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'py-1 px-1 outline-none block h-full w-full',
                'autocomplete': 'false'
            }),
            'userpic': forms.FileInput(attrs={

            })
        }

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }