import telebot

from settings import TELEGRAM_TOKEN

weather_bot = telebot.TeleBot(TELEGRAM_TOKEN)


@weather_bot.message_handler(commands=["start"])
def start(message):
    hello = (f"Привет, {message.from_user.first_name} рад тебя видеть!👋 "
             f"О погоде в каком городе ты сегодня хочешь узнать?")
    weather_bot.send_message(message.chat.id, hello)


@weather_bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()


weather_bot.polling(none_stop=True)
