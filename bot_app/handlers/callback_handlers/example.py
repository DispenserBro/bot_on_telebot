from telebot import types
from telebot.util import quick_markup

from keyboards.example_menu import menu_root as tmp
from starters.register_bot import bot


def send_example(callback_query: types.CallbackQuery):
    data = callback_query.data.split('_')
    match data:
        case [tmp.callback, *layers]:
            head = tmp
            for layer in layers:
                layer = int(layer)
                head = head.children[layer]
            msg_text = head.description
            buttons = head.get_buttons()

        case [tmp.callback]:
            msg_text = tmp.description
            buttons = tmp.get_buttons()

        case _:
            msg_text = 'WTF you just done???'
            buttons = {}

    bot.edit_message_text(
        msg_text,
        callback_query.message.chat.id,
        callback_query.message.id,
        parse_mode='MarkdownV2',
        reply_markup=quick_markup(buttons)
    )
    bot.answer_callback_query(callback_query.id)
