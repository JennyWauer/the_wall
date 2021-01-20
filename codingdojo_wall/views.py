from django.shortcuts import render, redirect

from .models import *

from login.models import User

def wall(request):
    if 'userid' in request.session:
        context = {
            "user": User.objects.get(id=request.session['userid']),
            "messages": Message.objects.all(),
            "comments": Comment.objects.all(),
        }
        return render(request, 'wall.html', context)
    redirect('/')

def add_message(request):
    if request.method == 'GET':
        return redirect('/wall')
    if request.method == 'POST':
        Message.objects.create(user_id=User.objects.get(id=request.session['userid']),message=request.POST['message'])
        return redirect('/wall')

def add_comment(request):
    if request.method == 'GET':
        return redirect('/wall')
    if request.method == 'POST':
        Comment.objects.create(user_id=User.objects.get(id=request.session['userid']),message_id=Message.objects.get(id=request.POST['message_id']),comment=request.POST['comment'])
        return redirect('/wall')

def delete(request):
    if request.method == 'GET':
        return redirect('/wall')
    if request.method == 'POST':
        if request.session['userid'] == int(request.POST['user_id']):
            comment_to_delete = Comment.objects.get(id=request.POST['comment_id'])
            comment_to_delete.delete()
            return redirect('/wall')
        return redirect('/wall')