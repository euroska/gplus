from functools import wraps
from django.http import HttpResponseForbidden, HttpResponseRedirect


def isAuthenticated(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if request.user is not None:
            return f(request, *args, **kwargs)

        return HttpResponseRedirect('/login/')

    return wrapper


def isAdmin(f):
    @wraps(f)
    def wrapper(request, *args, **kwargs):
        if request.user is not None and request.user.is_superadmin:
            return f(request, *args, **kwargs)

        return HttpResponseForbidden()
    return wrapper
