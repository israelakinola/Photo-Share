#Django imports
from django.contrib import admin
#Share imports
from .models import Photo, Like

admin.site.register([Photo, Like])
