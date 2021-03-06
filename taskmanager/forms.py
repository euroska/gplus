from django import forms
from .models import User


class LoginForm(forms.Form):
    '''
    Form for login user
    '''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        try:
            # check if password match
            user = User.objects.get(username=cleaned_data['username'])
            if not user.authenticate(cleaned_data['password']):
                self.add_error('password', 'Password does not match')

        except Exception as e:
            # username does not exists
            self.add_error('username', 'User does not exist')


