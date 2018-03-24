from functools import wraps
from django.http import HttpResponseRedirect
from .views import AuthView


def isAuthenticated(f):
    '''
    Decorator: user is logged
    '''
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if request.user is not None:
            return f(request, *args, **kwargs)

        return HttpResponseRedirect('/login/')

    return wrapper


def isAdmin(f):
    '''
    Decorator: user is superadmin
    '''

    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if request.user is not None and request.user.is_superadmin:
            return f(request, *args, **kwargs)

        return AuthView.as_view()(request, *args, **kwargs)

    return wrapper
