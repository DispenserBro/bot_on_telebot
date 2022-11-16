import telebot
import logging
import tomllib


with open('./config.toml', 'rb') as config:
    config = tomllib.load(config)

token = config['bot_info']['token']

telebot.logger.setLevel(logging.INFO)
logger = telebot.logger

bot = telebot.TeleBot(token)
