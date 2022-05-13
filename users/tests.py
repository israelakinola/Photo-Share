from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.models import User


class FunctionalTestCase(TestCase):
    """The testcase for all functional test is writting here"""

    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_loginpage(self):
        """This method test the login page"""
        # Go to the homepage
        self.browser.get("http://localhost:8000/login/")
        # fetch the login form
        fetch_login_form_ele = self.browser.find_element(By.TAG_NAME, "form")
        # check if it's present
        self.assertTrue(fetch_login_form_ele)

    def test_signuppage(self):
        """The method test the signup page"""
        # Go to the homepage
        self.browser.get("http://localhost:8000/signup/")
        # fetch the signup form
        fetch_login_form_ele = self.browser.find_element(By.TAG_NAME, "form")
        # check if it's present
        self.assertTrue(fetch_login_form_ele)

    def tearDown(self):
        self.browser.quit()


class UnitTestCase(TestCase):
    """The testcase for all functional test is wååritting here"""

    def test_signup_template(self):
        response = self.client.get("/login/")
        self.assertTemplateUsed(response, "users/login.html")

    def test_signup_template(self):
        response = self.client.get("/signup/")
        self.assertTemplateUsed(response, "users/signup.html")

    def test_user_obj(self):
        user = User.objects.create_user(
            username="test", email="test@email.com", password="test123"
        )
        self.assertEqual(user.email, "test@email.com")
