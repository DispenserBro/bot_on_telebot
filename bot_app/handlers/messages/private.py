from telebot import types
from telebot.util import quick_markup

from starters.register_bot import bot, logger
from keyboards.commands_menu import menu_root


def send_help(message: types.Message):
    logger.info(f'send_help triggered by user {message.from_user.username}')
    bot.send_message(
        chat_id=message.chat.id,
        text=menu_root.description,
        reply_markup=quick_markup(menu_root.get_buttons(), 1),
        parse_mode='MarkdownV2'
    )
