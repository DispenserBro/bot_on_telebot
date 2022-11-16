from telebot import types
from telebot.util import quick_markup

from starters.register_bot import bot, logger
from starters.get_commands_dict import commands_dict as commands
from keyboards.example_menu import menu_root


def send_help(message: types.Message):
    logger.info(f'send_help triggered by user {message.from_user.username}')
    all_commands = commands.values()
    all_commands = [[', '.join(["/" + cmd for cmd in list(el.values())[0]]), '- ' + list(el.values())[1]] for el in all_commands]
    commands_list = '\n\n'.join(' '.join(el) for el in all_commands)
    bot.reply_to(
        message, f"""\
        Привет, меня зовут @{bot.get_me().username}.
Вот список моих команд:\n
{commands_list}\
        """
)

def send_menu(message: types.Message):
    logger.info(f'send_menu triggered by user {message.from_user.username}')
    bot.send_message(
        chat_id=message.chat.id,
        text=menu_root.description,
        reply_markup=quick_markup(menu_root.get_buttons()),
        parse_mode='MarkdownV2'
    )

# def echo_message(message):
#     logger.info("echo_message triggered")
#     bot.reply_to(message, message.text)
