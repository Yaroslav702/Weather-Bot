import requests
from config import HEADERS

def get_html(url, params = None):
        return requests.get(url, headers=HEADERS, params=params)