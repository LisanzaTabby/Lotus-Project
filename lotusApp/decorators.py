from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')  
            response = view_func(request, *args, **kwargs)
            if response is None:
                raise ValueError("View function returned None instead of an HttpResponse.")
            return response
        return _wrapped_view
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to access this page!')
        return wrapper
    return decorator