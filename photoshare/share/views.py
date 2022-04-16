from dataclasses import field
import imp
from statistics import mode
from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from . import forms
from .models import Photo


class IndexView(LoginRequiredMixin, ListView):
    """ This class view handles the Home Index page view """
    template_name = 'share/home.html'
    context_object_name = 'photos'
    def get_queryset(self):
        """Return the last five published questions."""
        return Photo.objects.order_by('-date_shared')[:5]

class CreatePhotoView(LoginRequiredMixin, CreateView):
    """ This is a generic view class that handles the Create Photo form handling """
    model = Photo
    fields = ['url','caption']

    def form_valid(self, form):
        """ This method overides the Parent form_valid method to se the created_by 
        field before validating and save the form in the database """
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class UpdatePhotoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ This is a generic view class that handles the Create Photo form handling """
    model = Photo
    fields = ['url','caption']

    def form_valid(self, form):
        """ This method overides the Parent form_valid method to se the created_by 
        field before validating and save the form in the database """
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        """ This fucntion uses the UserPassTestMixin to validate the if the creator of the Photo obj
        is the same as the login user """
        photo = self.get_object()
        if photo.created_by == self.request.user:
            return True

    

class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ This class view delete a Photo from the view and database """
    model = Photo
    success_url = '/'

    def test_func(self):
        """ This fucntion uses the UserPassTestMixin to validate the if the creator of the Photo obj
        is the same as the login user """
        photo = self.get_object()
        if photo.created_by == self.request.user:
            return True
        return False

