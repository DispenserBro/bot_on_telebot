from telebot import types

from starters.register_bot import bot, logger


def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


def echo_message(message):
    logger.info("echo_message triggered")
    bot.reply_to(message, message.text)
