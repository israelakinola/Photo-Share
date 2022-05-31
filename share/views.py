from dataclasses import field
from statistics import mode
from urllib import request
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from . import forms
from .models import Photo, Like


class IndexView(LoginRequiredMixin, ListView):
    """This class view handles the Home Index page view"""

    template_name = "share/home.html"
    context_object_name = "photos"

    def get_queryset(self):

        """Return the last five published questions."""
        return Photo.objects.order_by("-date_shared")[:5]

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        context["liked_photos"] = Photo.objects.filter(
            like__from_user=self.request.user.id
        )
        return context


class CreatePhotoView(LoginRequiredMixin, CreateView):
    """This is a generic view class that handles the Create Photo form handling"""

    model = Photo
    fields = ["image", "caption"]

    def form_valid(self, form):
        """This method overides the Parent form_valid method to se the created_by
        field before validating and save the form in the database"""
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UpdatePhotoView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """This is a generic view class that handles the Create Photo form handling"""

    model = Photo
    fields = ["image", "caption"]

    def form_valid(self, form):
        """This method overides the Parent form_valid method to se the created_by
        field before validating and save the form in the database"""
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """This method uses the UserPassTestMixin to validate the if the creator of the Photo obj
        is the same as the login user"""
        photo = self.get_object()
        if photo.created_by == self.request.user:
            return True


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """This class view delete a Photo from the view and database"""

    model = Photo
    success_url = "/"

    def test_func(self):
        """This method uses the UserPassTestMixin to validate the if the creator of the Photo obj
        is the same as the login user"""
        photo = self.get_object()
        if photo.created_by == self.request.user:
            return True
        return False


def photo_like(request):
    """This method handles the like photo XMLHttpRequest"""
    photo = Photo.objects.get(pk=request.GET["photo_id"])
    liked_photos = Photo.objects.filter(like__from_user=request.user.id)
    if photo not in liked_photos:
        like = Like(from_user=request.user, to_photo=photo)
        like.save()
        return JsonResponse({"status": "like", "like_count": photo.like_set.count()})
    else:
        like_obj = Like.objects.filter(from_user=request.user.id, to_photo=photo.id)
        like_obj.delete()
        return JsonResponse({"status": "unlike", "like_count": photo.like_set.count()})
