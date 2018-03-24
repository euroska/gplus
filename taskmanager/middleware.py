from .models import User
from .views import LoginView


class AuthMiddleware:
    '''
    Very simple auth middleware
    '''
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        '''
        Easy method to get logged user
        '''
        request.user = None
        username = request.session.get('user', None)

        if username is not None:
            try:
                request.user = User.objects.get(username=username)
            except Exception as e:
                pass

        return self.get_response(request)

