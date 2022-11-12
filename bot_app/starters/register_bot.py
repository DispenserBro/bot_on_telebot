import telebot
import logging
import tomllib


with open('./config.toml', 'rb') as config:
    config = tomllib.load(config)

token = config['bot_info']['token']

telebot.logger.setLevel(logging.INFO)
logger = telebot.logger

bot = telebot.TeleBot(token)


from handlers.utils.weather import send_weather_image
from handlers.messages.default import send_welcome, echo_message


bot.register_message_handler(
    send_welcome,
    commands=['help', 'start']
)

bot.register_message_handler(
    send_weather_image,
    commands=['w', 'weather', 'погода']
)

bot.register_message_handler(
    echo_message,
    func=lambda message: True
)
