from django.test import TestCase
from selenium import webdriver


class FunctionalTestCase(TestCase):
    """ The testcase for all functional test is writting here """

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

class UnitTestCase(TestCase):
    """ The testcase for all functional test is wååritting here """
    pass
