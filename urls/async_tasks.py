import requests
from bs4 import BeautifulSoup


def update_url_title(url_instance):
    """Updates the title of the URL instance."""
    try:
        response = requests.get(url_instance.full_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        url_instance.title = soup.title.string
        url_instance.save()
    except Exception as e:
        print(e)