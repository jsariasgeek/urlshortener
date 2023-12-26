from django.test import TestCase

# Create your tests here.
class URLTest(TestCase):
    def test_short_url(self):
        response = self.client.post('/short/', data={"url":"https://www.google.com"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('url'), "https://www.google.com")
        self.assertTrue(response.json().get('shorted_url'))