from utils.get_html import get_html
from utils.get_sinoptik_url import get_sinoptik_url

def parse(city, content_fn):
        html = get_html(get_sinoptik_url(city))
        if html.status_code == 200:
            return content_fn(html.text)
        else:
            print('Error')