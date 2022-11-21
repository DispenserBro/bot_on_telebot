import logging
import tomllib
import os.path
import telebot
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

with open(os.path.join(BASE_DIR, 'config.toml'), 'rb') as config:
    config = tomllib.load(config)

token = config['bot_info']['token']

telebot.logger.setLevel(logging.INFO)
logger = telebot.logger

bot = telebot.TeleBot(token)
