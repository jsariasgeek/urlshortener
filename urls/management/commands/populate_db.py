import asyncio
import requests
from django.core.management.base import BaseCommand, CommandError   
from urls.models import URL
from asgiref.sync import sync_to_async
import aiohttp


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


async def visit_shorted_url(url, session):
    async with session.get(url.shorted_url) as response:
        print(response.history[0] if response.history else response)

async def get_urls():
    return await sync_to_async(list)(URL.objects.all())

async def visit_shorted_urls():
    urls = await get_urls()
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(visit_shorted_url(url, session)) for url in urls]
        await asyncio.gather(*tasks)

class Command(BaseCommand):
    help = "Populate db with URLS"

    def handle(self, *args, **options):
        create_shorted_urls()
        asyncio.run(visit_shorted_urls())