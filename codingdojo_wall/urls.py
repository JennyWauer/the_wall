from django.urls import path

from . import views

urlpatterns = [
    path('', views.wall),
    path('add_message', views.add_message),
]