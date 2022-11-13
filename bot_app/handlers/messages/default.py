from telebot import types
from telebot.custom_filters import IsAdminFilter

from starters.register_bot import bot, logger
from starters.get_commands_dict import commands_dict as commands


def send_help(message):
    all_commands = commands.values()
    all_commands = [[', '.join(["/" + cmd for cmd in list(el.values())[0]]), '- ' + list(el.values())[1]] for el in all_commands]
    commands_list = '\n'.join(' '.join(el) for el in all_commands)
    bot.reply_to(message, f"""\
Привет, меня зовут @{bot.get_me().username}.
Вот список моих команд:
{commands_list}
\
""")


def echo_message(message):
    logger.info("echo_message triggered")
    bot.reply_to(message, message.text)
