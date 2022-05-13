from unicodedata import name
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models import Photo, Like
from django.contrib.auth.models import User


class FunctionalTestCase(TestCase):
    """The testcase for all functional test is writting here"""

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_homepage(self):
        # Go to the homepage
        self.browser.get("http://localhost:8000")
        # fetch the login form
        fetch_login_form_ele = self.browser.find_element(By.TAG_NAME, "form")
        # check if it's present
        self.assertTrue(fetch_login_form_ele)

    def tearDown(self):
        self.browser.quit()


class UnitTestCase(TestCase):
    """The testcase for all functional test is wååritting here"""

    def test_photo_obj(self):
        user = User.objects.create_user(
            username="test2", email="test2@email.com", password="test123"
        )
        photo = Photo()
        photo.url = "avi.jpg"
        photo.caption = "test photo"
        photo.created_by = user
        photo.save()
        self.assertEqual(photo.caption, "test photo")

    def test_like_obj(self):
        user = User.objects.create_user(
            username="test2", email="test2@email.com", password="test123"
        )
        photo = Photo.objects.create(
            url="avi2.jpg", caption="Test Photo", created_by=user
        )
        like = Like()
        like.to_photo = photo
        like.from_user = user
        like.save()
        self.assertEqual(Like.objects.filter(to_photo=photo).count(), 1)
