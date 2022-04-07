from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Photo(models.Model):
    photo_url = models.TextField()
    photo_caption = models.TextField()
    date_shared = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
