import json

import requests
import telebot

from settings import TELEGRAM_TOKEN, OPEN_WEATHER_API

weather_bot = telebot.TeleBot(TELEGRAM_TOKEN)


@weather_bot.message_handler(commands=["start"])
def start(message):
    """ Функция приветствия пользователя """
    hello = (f"Привет, {message.from_user.first_name} рад тебя видеть!👋 "
             f"О погоде в каком городе ты сегодня хочешь узнать?")
    weather_bot.send_message(message.chat.id, hello)


@weather_bot.message_handler(content_types=["text"])
def get_weather(message):
    """ Функция запроса от пользователя города и отображения погоды """
    city = message.text.strip().lower()
    # Отправляем запрос на OpenWeather
    weather_service = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPEN_WEATHER_API}&units=metric")
    if weather_service.status_code == 200:
        data = json.loads(weather_service.text)
        message_weather = (f"Погода в городе {city.title()}, страна {data["sys"]["country"]}\n"
                           f"Температура {round(data["main"]["temp"])}°C\n"
                           f"Влажность воздуха {data["main"]["humidity"]}%\n"
                           f"Давление {data["main"]["pressure"]}гПа\n"
                           f"Скорость ветра {round(data["wind"]["speed"])} м/с")
        weather_bot.reply_to(message, message_weather)
    else:
        message_weather = "Извините, но я не знаю ничего о погоде в этом городе😔"
        weather_bot.reply_to(message, message_weather)


weather_bot.polling(none_stop=True)
