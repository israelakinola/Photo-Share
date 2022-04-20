from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Photo(models.Model):
    """ 
    This class setups the Photo Object Model 
    Attributes:
        url :  Photo image file
        caption : Photo caption
        date_shared : The date the photo was created/shared
        created : The User object who created the Photo object

    """
    url = models.ImageField(upload_to='photos')
    caption = models.TextField()
    date_shared = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """ This method redirect back to the homepage whenever a Photo object is save()  """
        return reverse('share.home')
