import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models

def home(request):
    """ This func handle the view for the Home View Page"""
    context = {
        'title': 'Home',
        'photos': models.Photo.objects.all()
    }
    return render(request, 'share/home.html', context)

