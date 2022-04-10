import re
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignupForm
from django.contrib import messages

def signup(request):
    """ This function handles the Signup view """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"User Successfully Created {username}")
            return redirect('share.home')
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form' : form})
