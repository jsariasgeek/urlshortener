import json
from django.urls import reverse
from django.test import TestCase
from urls.async_tasks import update_url_title
from urls.models import URL

class URLViewsTestCase(TestCase):
    def setUp(self):
        self.websites = []
        with open('urls/websites.txt', 'r') as f:
            websites = f.readlines()
            for website in websites[:3]:
                url_instance = URL.objects.create(full_url=website.strip())
                self.websites.append(website.strip())
                update_url_title(url_instance.key)

    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_shorten_url(self):
        response = self.client.post(reverse('short_url'), data=json.dumps({"url": "https://google.com"}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_top_100_most_accessed_urls(self):
        response = self.client.get(reverse('top_100_most_accessed_urls'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['urls']), 3)
        assert response.json()['urls'][0]['full_url'] in self.websites
        assert response.json()['urls'][1]['full_url'] in self.websites
        assert response.json()['urls'][2]['full_url'] in self.websites

        # self.assertTemplateUsed(response, 'top_100.html')