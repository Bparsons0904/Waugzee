from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm



class UpdateUser(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')



    # username = forms.CharField(label='User Name', max_length=150, required=False)
    # first_name = forms.CharField(label='First Name', max_length=30, required=False)
    # last_name = forms.CharField(label='Last Name', max_length=150, required=False)
    # email = forms.CharField(label='Email Address', required=False)
