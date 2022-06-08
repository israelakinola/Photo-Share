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

    image = models.ImageField(upload_to="photos")
    caption = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_shared = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    def get_absolute_url(self):
        """This method redirect users back to the homepage whenever a Photo object is save()"""
        return reverse("share.home")


class Like(models.Model):
    """
    This class setups the Like Object Model
    Attributes:
        from_user :  The login user like the photo
        to_photo : The Photo that is being liked
        date_liked : The date the photo was liked

    """
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    dated_liked = models.DateTimeField(default=timezone.now)
