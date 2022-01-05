import requests
from bs4 import BeautifulSoup

city = input('Назвіть місто: ')
URL = 'https://ua.sinoptik.ua/погода-' + city.lower()
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'accept': '*/*'
}

def get_html(url, params = None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    weather = []
    soup = BeautifulSoup(html, 'html.parser')
    weather_description = soup.find('div', class_='description').get_text(strip=True)
    min_temp = soup.find('div', class_='min').get_text()
    max_temp = soup.find('div', class_='max').get_text()
    weather.append(
        {
            'description': weather_description,
            'minimum': min_temp,
            'maximuum': max_temp
        }
    )
    print(weather)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')



parse()