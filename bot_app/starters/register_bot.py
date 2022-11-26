import logging
import os.path
import telebot
from yaml import load, Loader
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

with open(os.path.join(BASE_DIR, 'config.yaml'), 'rb') as config:
    config = load(config, Loader)

token = config['bot_info']['token']

telebot.logger.setLevel(logging.INFO)
logger = telebot.logger

bot = telebot.TeleBot(token)
