from django.db import models

from urls.url_shortener import URLShortener

# Create your models here.
class URL(models.Model):
    full_url = models.CharField(max_length=2048, unique=True)
    shorted_url = models.CharField(max_length=256, unique=True)
    key = models.CharField(max_length=256, unique=True) # This is the key that will be used to retrieve the original URL
    title = models.CharField(max_length=256)
    access_counter = models.IntegerField(default=0)

    def create_shorted_url(self, value):
        shortener = URLShortener()
        short_url, key = shortener.shorten_url(self.full_url)
        self.shorted_url = short_url
        self.key = key

    def as_dict(self):
        return {
            "full_url": self.full_url,
            "shorted_url": self.shorted_url,
            "title": self.title,
        }

    def save(self, *args, **kwargs):
        self.create_shorted_url(self.full_url)
        super(URL, self).save(*args, **kwargs)