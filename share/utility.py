from django.http import HttpResponse, JsonResponse

#Share imports
from . import forms
from .models import Photo, Like

def like_and_unlike_photo(request, photo, liked_photos ):
    #Check if there is no like db object from any of the returned photos
    if photo not in liked_photos:
        #Create a Like db obj for photo
        like = Like(from_user=request.user, to_photo=photo)
        like.save()
        return JsonResponse({"status": "like", "like_count": photo.like_set.count()})
    else:
        #Delete a Like db obj for photo if photo was already liked
        like_obj = Like.objects.filter(from_user=request.user.id, to_photo=photo.id)
        like_obj.delete()
        #Return a Json Response
        return JsonResponse({"status": "unlike", "like_count": photo.like_set.count()})

