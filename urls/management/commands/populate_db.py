import asyncio
import requests
from django.core.management.base import BaseCommand, CommandError   
from urls.models import URL
from asgiref.sync import sync_to_async
import aiohttp

async def create_shorted_url(url, session):
    """
    Asynchronously create a shortened url
    """
    async with session.post('http://localhost:8000/urls/short/', json={"url": url}) as response:
        print(await response.json())

async def create_shorted_urls():
    """
    Asynchronously create 100 shortened urls
    """
    async with aiohttp.ClientSession() as session:
        with open('urls/websites.txt', 'r') as f:
            websites = f.readlines()
            # i want to create chunks of 10 websites and run an event loop for each chunk
            # this is because my server can crash
            chunks = [websites[x:x+20] for x in range(0, len(websites), 20)]
            for chunk in chunks:
                print('running chunk')
                tasks = [asyncio.create_task(create_shorted_url(website.strip(), session)) for website in chunk]
                await asyncio.gather(*tasks)


    # Delete urls with no title: sometimes those pages are not accessible
    await sync_to_async(URL.objects.filter(title="").delete)()


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
        asyncio.run(create_shorted_urls())
        asyncio.run(visit_shorted_urls())