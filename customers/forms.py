from django import forms
from customers.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


class ProfileSignupForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = [
            # "first_name",
            # "last_name",
            "phone_number",
            "address",
            "city",
            "state",
            "zip_code",
        ]


