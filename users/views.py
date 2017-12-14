from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django import forms

def index(request):
    return render(request, 'lists/index.html')

def logout_view(request):
    logout(request)
    return render(request, 'lists/index.html')
