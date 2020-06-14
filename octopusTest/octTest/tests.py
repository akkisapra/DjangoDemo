from django.test import TestCase

from selenium import webdriver

class FunctionalTestCase(TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_there_is_homepage(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("hello", self.browser.page_source)

class UnitTestCase(TestCase):
    def test_home_homepage_template(self):
        response =self.client.get("/")
        self.assertTemplateUsed(response,'test/home.html')


