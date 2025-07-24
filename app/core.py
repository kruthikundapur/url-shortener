import random
import string

class URLShortener:
    def __init__(self):
        self.url_map = {}
    
    def shorten(self, long_url):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        self.url_map[code] = {
            "url": long_url,
            "clicks": 0,
            "created_at": "2023-01-01"  # We'll improve this later
        }
        return code

    def get_url(self, code):
        return self.url_map.get(code)