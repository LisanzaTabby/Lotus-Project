from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            is_dataentry = request.user.groups.filter(name='Dataentry').exists()
            is_finance = request.user.groups.filter(name='Finance').exists()
            is_donor = request.user.groups.filter(name='Donor').exists()
            if is_dataentry:
                return redirect('dataentry')
            elif is_finance:
                return redirect('finance')
            elif is_donor:
                return redirect('donor')
            else:
                return HttpResponse('You are not an Authorized user! Please Contact the Admin Support')

        else:
            return view_func(request, *args, **kwargs)
    return wrapper
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