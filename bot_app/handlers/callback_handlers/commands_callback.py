from telebot import types
from telebot.util import quick_markup

from keyboards.commands_menu import menu_root as cmd_root
from starters.register_bot import bot


def send_menu(callback_query: types.CallbackQuery) -> None:
    data = callback_query.data.split('_')
    match data:
        case [cmd_root.callback, *layers]:
            head = cmd_root
            for layer in layers:
                layer = int(layer)
                head = head.children[layer]
            msg_text = head.description
            buttons = head.get_buttons()

        case [cmd_root.callback]:
            msg_text = cmd_root.description
            buttons = cmd_root.get_buttons()

        case _:
            msg_text = 'WTF you just done???'
            buttons = {'Назад': {'callback_data': cmd_root.callback}}

    bot.edit_message_text(
        msg_text,
        callback_query.message.chat.id,
        callback_query.message.id,
        parse_mode='MarkdownV2',
        reply_markup=quick_markup(buttons, 1)
    )

    bot.answer_callback_query(callback_query.id)
