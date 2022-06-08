from django.test import TestCase
from django.contrib.auth.models import User


class UsersViewTest(TestCase):

    def test_login_view_template(self):
        response = self.client.get("/login/")
        self.assertTemplateUsed(response, "users/login.html")

    def test_signup_view_template(self):
        response = self.client.get("/signup/")
        self.assertTemplateUsed(response, "users/signup.html")
