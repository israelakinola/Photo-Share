from dataclasses import field
import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    """ This class extends the User creation form class and add an email field """

    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']