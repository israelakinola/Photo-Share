from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """ This func handle the view for the Home View"""
    context = {
        'title': 'Home',
        'photos': 'photos'
    }
    return render(request, 'share/home.html', context)

