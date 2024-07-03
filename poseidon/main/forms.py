from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm

from .models import BaseUser


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)

    class Meta:
        model = BaseUser
        fields = ('username', 'phone', 'email', 'otchestvo', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Имя', widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = BaseUser
        fields = ('username', 'first_name', 'last_name', 'otchestvo', 'email', 'phone')
