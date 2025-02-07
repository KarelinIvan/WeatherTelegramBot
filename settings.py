import os

from dotenv import load_dotenv

load_dotenv()

# Для работы с сервисом telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Для работы с сервисом OpenWeather
OPEN_WEATHER_API = os.getenv("OPEN_WEATHER_API")
