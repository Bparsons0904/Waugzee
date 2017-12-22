from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
# from django import forms
# from django.views.generic import View
from users.forms import UpdateUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm



from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'lists/index.html')

def logout_view(request):
    logout(request)
    return render(request, 'lists/index.html')

def user_info(request):
    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateUser(instance=request.user)
    return render(request, 'users/userupdate.html', {'form': form})

# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, _('Please correct the error below.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })
