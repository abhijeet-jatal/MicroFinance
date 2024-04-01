from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "ex.xyz@gmail.com",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


role_choice = (
    ('Operational Manager', 'Operational Manager'),
    ('Relation Manager', 'Relation Manager'),
    ("Customer", "Customer")
)


class SignUpForm(UserCreationForm):
    fullname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "ex.xyz@gmail.com",
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    role = forms.ChoiceField(label='Role', choices=role_choice, widget=forms.Select())

    class Meta:
        model = User
        fields = ('username', 'fullname', 'password1', 'password2', 'role')


'''
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_relation', 'is_operational', 'is_customer')
'''
