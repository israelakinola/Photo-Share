from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from .models import Photo

class PostAPhotoForm(forms.ModelForm):
    """ This class setup a model from for the Photo model """
    class Meta():
        model = Photo
        fields = ['url','caption',]