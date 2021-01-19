from django.shortcuts import render, redirect

from .models import *

from login.models import User

def wall(request):
    return render(request, 'wall.html')