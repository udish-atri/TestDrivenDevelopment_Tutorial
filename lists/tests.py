from django.test import TestCase


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_renders_home_page_content(self):
        response = self.client.get("/")
        self.assertContains(response, "To-Do")
