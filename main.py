from telegram.ext import Updater, CommandHandler

from weather.current_weather import current_weather
from weather.storm import storm_attention


def start(update, context):
    message = 'Вас вітає Sinoptik Bot - актуальна погода. \nДля перегляду доступних команд - /help.'
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text = message)

def help(update, context):
    message = 'Доступні команди та їх функції: \n/weather Назва міста - дізнатися поточну погоду в обраному місті \n/storm Назва міста - перевірити наявність штормового попередження'
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text = message)


updater = Updater("5087818773:AAHOjeWhI6CB5BV3atz7xQSZOdK3yoCdqt4")
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("weather", current_weather))
dispatcher.add_handler(CommandHandler("storm", storm_attention))


updater.start_polling()
updater.idle()