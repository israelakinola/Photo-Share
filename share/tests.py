#Django and Third Party Libary Imports
from unicodedata import name
from django.test import TestCase
<<<<<<< HEAD
#Share imports
=======
>>>>>>> 538598d80ee5f99ff256a1886b27b2c1894045c6
from .models import Photo, Like
from django.contrib.auth.models import User

class ShareModelTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="test_user", email="test2@email.com", password="test123"
        )

        # Create a photo
        self.photo = Photo()
        self.photo.url = "avi.jpg"
        self.photo.caption = "test photo"
        self.photo.created_by = self.user
        # Save photo
        try:
            self.photo.save()
        except:
            print("Couldn't save Photo to Database")

    def test_if_photo_is_created_and_retrived_from_db(self):
        # Get the fist photo from the database
        try:
            recent_photo = Photo.objects.all().first()
        except:
            print("Couldn't Get Photo from Database")

        # Check if recent_photo creator ('test_user') have the user name 'test_user'
        self.assertEqual(recent_photo.created_by.username, "test_user")
    
    def test_if_photo_is_updated(self):
        # Update Photo object and save to DB
        self.photo = Photo.objects.all().first()
        self.photo.caption = "Update Photo"
        try:
            self.photo.save()
        except:
            print("Couldn't Save Photo to Database")

        # Get the fist photo from the database
        try:
            recent_photo = Photo.objects.all().first()
        except:
            print("Couldn't Get Photo from Database")

        # Check if recent_photo creator ('test_user') caption is equal to 'Update Photo'
        self.assertEqual(recent_photo.caption, "Update Photo")

    def test_if_like_obj_is_liked(self):
        # Create a Like Object
        like = Like()
        like.to_photo = self.photo
        like.from_user = self.user
        try:
            # Save to database
            like.save()
        except:
            print("Couldn't Save Like to Database")

        # Check if the Photo(self.photo) likes objects is equal to one
        self.assertEqual(Like.objects.filter(to_photo=self.photo).count(), 1)

    def test_if_like_obj_is_unlikde(self):
        try:
            #Get a recent like
            recent_photo_like = Like.objects.all().first()
            recent_photo_like.delete()
        except:
            print("Couldn't Delete Like from the Database")

        # Check if the Photo(self.photo) likes objects is equal to 0
        self.assertEqual(Like.objects.filter(to_photo=self.photo).count(), 0)

    def test_if_photo_is_deleted_from_db(self):
        # Get the fist photo from the database
        try:
            recent_photo = Photo.objects.all().first()
        except:
            print("Couldn't Get Photo from Database")
        recent_photo.delete()

        # Check if recent_photo creator ('test_user') have the user name 'test_user'
        self.assertEqual(recent_photo.id, None)
