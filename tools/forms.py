from django.contrib.auth.forms import AuthenticationForm
from django import forms


class LoginForm(AuthenticationForm):
    """LoginForm
    Form inherited from AuthenticationForm used for the user login
    Main goal is to use widget to get a good UI
    """

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].required = True
        self.fields['username'].widget = forms.TextInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'E-mail',
                                        'name': 'email',
                                        'type': 'email',
                                        'autofocus': ''
                                    }
        )

        self.fields['password'].required = True
        self.fields['password'].widget = forms.PasswordInput(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Password',
                                        'name': 'password',
                                        'type': 'password',
                                    }
        )
