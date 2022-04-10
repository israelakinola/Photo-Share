import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import models

@login_required
def home(request):
    """ This function handle the view for the Home View Page """
    context = {
        'title': 'Home',
        'photos': models.Photo.objects.all()
    }
    return render(request, 'share/home.html', context)

