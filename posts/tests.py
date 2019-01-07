from django.urls import resolve
from django.test import TestCase
from posts.views import index


class HomePageTest(TestCase):

    def test_resolve_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, index)