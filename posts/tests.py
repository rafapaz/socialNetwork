from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from posts.views import index


class HomePageTest(TestCase):

    def test_resolve_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')        
        html = response.content.decode('utf8')
        self.assertIn('html', html)
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
