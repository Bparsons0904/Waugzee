from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField

class SignUpForm(UserCreationForm):
    bio = forms.CharField(help_text="Optional.")
    location = forms.CharField(help_text="Optional.")
    birth_date = forms.DateField(help_text='Optional. Format: YYYY-MM-DD')
    phone_number = PhoneNumberField()
    profile_picture = forms.ImageField(help_text="Optional.")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'bio', 'location', 'birth_date', 'profile_picture', )
