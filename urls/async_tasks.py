import requests
from bs4 import BeautifulSoup
from celery import shared_task
from urls.models import URL

@shared_task
def update_url_title(url_instance_key):
    """Updates the title of the URL instance."""
    url_instance = URL.objects.get(key=url_instance_key)
    response = requests.get(url_instance.full_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    if soup.title:
        url_instance.title = soup.title.string
        url_instance.save()
