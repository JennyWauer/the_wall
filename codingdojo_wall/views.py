from django.shortcuts import render, redirect

from .models import *

from login.models import User

def wall(request):
    context = {
        "user": User.objects.filter(id=request.session['userid']),
    }
    return render(request, 'wall.html', context)