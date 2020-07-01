from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  
        return view_function(request, *args, **kwargs)
    return wrapper

def allowed_users(allowed_roles=[]):
    def decorator(view_function):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.exists():
                group = request.user.groups.first().name
                if group in allowed_roles:
                    return view_function(request, *args, **kwargs)
            return HttpResponse('You are not allowed to view this page')
        return wrapper
    return decorator
