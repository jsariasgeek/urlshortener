import hashlib
import string
from .config import BASE_DOMAIN

class URLShortener:
    def __init__(self):
        self.url_map = {}
        self.base_domain = BASE_DOMAIN

    def _generate_key(self, original_url):
        """Generates a unique key for the URL."""
        hasher = hashlib.sha256()
        hasher.update(original_url.encode())
        return self._base62_encode(int(hasher.hexdigest(), 16))[:8]  # Taking the first 8 characters for simplicity

    def _base62_encode(self, number):
        """Encodes a number into base62."""
        characters = string.digits + string.ascii_letters
        base = len(characters)
        encoded = ""
        while number > 0:
            number, rem = divmod(number, base)
            encoded = characters[rem] + encoded
        return encoded or '0'

    def shorten_url(self, original_url):
        """Shortens the URL and returns the shortened version."""
        key = self._generate_key(original_url)
        shortened_url = self.base_domain + key
        self.url_map[key] = original_url
        return shortened_url, key

    def get_original_url(self, short_url):
        """Retrieves the original URL from the shortened version."""
        key = short_url.replace(self.base_domain, "")
        return self.url_map.get(key, None)
