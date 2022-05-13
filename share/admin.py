from django.contrib import admin
from .models import Photo, Like

admin.site.register([Photo, Like])
