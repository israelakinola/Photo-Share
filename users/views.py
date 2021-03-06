#Django and Third Party Libary Imports
import re
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import UserPassesTestMixin


def welcome(request):
    """ This function handles the welcome view for none authenticated users"""
    return render(request, "users/welcome.html")
    
def signup(request):
    """This function handles the Signup view and Form Handling"""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"User Successfully Created {username}")
            return redirect("share.home")
    else:
        form = SignupForm()
    return render(request, "users/signup.html", {"form": form})


class UsersLoginView(LoginView):
    template_name = "users/login.html"
