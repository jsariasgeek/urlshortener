from django.contrib import admin
from django.urls import path, include
from .views import short_url, top_100_most_accessed_urls

urlpatterns = [
    path('short/', view=short_url, name='short_url'),
    path('top-100/', view=top_100_most_accessed_urls, name='top_100_most_accessed_urls')

]
