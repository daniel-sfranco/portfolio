from django.shortcuts import render
from .models import User

def register(request):
    return render(request, 'users/register.html')