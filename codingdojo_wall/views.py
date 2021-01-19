from django.shortcuts import render, redirect

from .models import *

from login.models import User

def wall(request):
    context = {
        "user": User.objects.filter(id=request.session['userid']),
    }
    return render(request, 'wall.html', context)

def add_message(request):
    if request.method == 'GET':
        return redirect('/wall')
    if request.method == 'POST':
        Message.objects.create(user_id=request.POST['user_id'],message=request.POST['message'])
        return redirect('/wall')

def add_comment(request):
    if request.method == 'GET':
        return redirect('/wall')
    if request.method == 'POST':
        Comment.objects.create(user_id=request.POST['user_id'],message_id=request.POST['message_id'],comment=request.POST['comment'])
        return redirect('/wall')