import requests
from django.core.management.base import BaseCommand, CommandError   
from urls.models import URL


def create_shorted_urls():
    """
    Create 100 shorted urls
    """
    with open('urls/websites.txt', 'r') as f:
        websites = f.readlines()
        for website in websites:
            website = website.strip()
            response = requests.post('http://localhost:8000/urls/short/', json={"url":website})
            print(response.json())
    
    # delete urls with no title: sometimes those pages are not accesible
    urls_to_delete = URL.objects.filter(title="")
    urls_to_delete.delete()


def visit_shorted_urls():
    urls = URL.objects.all()
    for url in urls:
        response = requests.get(url.shorted_url)
        print(response.history[0])

class Command(BaseCommand):
    help = "Populate db with URLS"

    def handle(self, *args, **options):
        create_shorted_urls()
        visit_shorted_urls()