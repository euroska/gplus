from .models import User
from .views import LoginView


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        request.user = None
        username = request.session.get('user', None)

        if username is not None:
            try:
                request.user = User.objects.get(username=username)
            except Exception as e:
                pass

        return self.get_response(request)

