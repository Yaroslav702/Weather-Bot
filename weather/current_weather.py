from bs4 import BeautifulSoup
from utils.parse import parse
from utils.get_city_from_user_input import get_city_from_user_input
from utils.soup_find_text import get_soup_text


def current_weather(update, context):
    user_city = get_city_from_user_input(update.message.text) 
    
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        city_name = get_soup_text(soup, 'div', 'cityName')        
        weather_description = get_soup_text(soup, 'div', 'description')
        min_temp = get_soup_text(soup, 'div', 'min')
        max_temp = get_soup_text(soup, 'div', 'max')
        weather = (city_name, weather_description.strip(), min_temp, max_temp)
        return '\n'.join(weather)
    
    text = parse(user_city, get_content)
    chat = update.effective_chat
    if user_city == 'Введіть команду правильно: /команда назва міста':
        context.bot.send_message(chat_id=chat.id, text = user_city)
    else:
        context.bot.send_message(chat_id=chat.id, text = text)

        
