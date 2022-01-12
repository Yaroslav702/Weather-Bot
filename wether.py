from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup

def start(update, context):
    message = 'Вас вітає Sinoptik Bot - актуальна погода. \nДля перегляду доступних команд - /help.'
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text = message)

def help(update, context):
    message = 'Доступні команди та їх функції: \n/weather Назва міста - дізнатися поточну погоду в обраному місті \n/storm Назва міста - перевірити наявність штормового попередження'
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text = message)

def current_weather(update, context):
    user_input = update.message.text
    user_input = user_input.split()
    user_city = user_input[1]

    URL = 'https://ua.sinoptik.ua/погода-' + user_city.lower()
    HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'accept': '*/*'}

    def get_html(url, params = None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        city_name = soup.find('div', class_='cityName').get_text()
        weather_description = soup.find('div', class_='description').get_text(strip=True)
        min_temp = soup.find('div', class_='min').get_text()
        max_temp = soup.find('div', class_='max').get_text()

        weather = (city_name, weather_description, min_temp, max_temp)
        return '\n'.join(weather)

    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            return get_content(html.text)
        else:
            print('Error')

    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text = parse())
    
    
    
def storm_attention(update, context):
    user_input = update.message.text
    user_input = user_input.split()
    user_city = user_input[1]

    URL = 'https://ua.sinoptik.ua/погода-' + user_city.lower()
    HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'accept': '*/*'}

    def get_html(url, params = None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        city_name = soup.find('div', class_='cityName').get_text()
        storm_attention = soup.find('div', class_='ico-stormWarning-1')
        if storm_attention:
            return f'{city_name}\nДіє штормове попередження. Обережно!⚠️'
        else:
            return f'{city_name}\nШтормове попередження відсутнє. Спокійно😌'

    def parse():
        html = get_html(URL)
        if html.status_code == 200:
            return get_content(html.text)
        else:
            print('Error')


    chat = update.effective_chat

    context.bot.send_message(chat_id=chat.id, text = parse())

updater = Updater("5087818773:AAHOjeWhI6CB5BV3atz7xQSZOdK3yoCdqt4")
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("weather", current_weather))
dispatcher.add_handler(CommandHandler("storm", storm_attention))


updater.start_polling()
updater.idle()