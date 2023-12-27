from urls.models import URL
from django.test import TestCase
from django.db import IntegrityError

class URLModelTestCase(TestCase):
    def setUp(self):
        self.url = URL.objects.create(full_url="https://www.google.com")
    
    def test_short_url(self):
        self.assertTrue(self.url.shorted_url)
    
    def test_short_url_is_unique(self):
        with self.assertRaises(IntegrityError):
            URL.objects.create(full_url="https://www.google.com")