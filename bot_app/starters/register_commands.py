from telebot import TeleBot

from handlers.messages import private, groups, admin
from handlers.utils import weather
from handlers.callback_handlers import commands_callback

from starters.get_commands_dict import commands_to_register as ALL_COMMANDS
from starters.register_bot import logger  # , bot


def registrer_admin_msg_handlers(bot: TeleBot) -> None:
    bot.register_message_handler(
        admin.admin_mute_member,
        func=lambda m: m.text and m.text.startswith('!ro'),
        chat_types=['group', 'supergroup']
    )

    bot.register_message_handler(
        admin.admin_ban_member,
        func=lambda m: m.text == '!ban',
        chat_types=['group', 'supergroup']
    )

    bot.register_message_handler(
        admin.admin_pardon_member,
        func=lambda m: m.text and m.text.startswith('!pardon '),
        chat_types=['group', 'supergroup']
    )

    logger.info('admin_msg_handlers registered')


def register_private_msg_handlers(bot: TeleBot) -> None:
    bot.register_message_handler(
        private.send_help,
        commands=ALL_COMMANDS['help'],
        chat_types=['private']
    )

    logger.info('private_msg_handlers registered')


def register_group_msg_handlers(bot: TeleBot) -> None:
    bot.register_message_handler(
        groups.answer_a,
        regexp=r'.*[Аа]\.',
        chat_types=['group', 'supergroup']
    )

    logger.info('group_msg_handlers registered')


def register_utils_handlers(bot: TeleBot) -> None:
    bot.register_message_handler(
        weather.send_weather_image,
        commands=ALL_COMMANDS['weather1']
    )

    bot.register_message_handler(
        weather.send_w2_info,
        commands=ALL_COMMANDS['weather2']
    )

    logger.info('utils_handlers registered')


def register_callback_query_handlers(bot: TeleBot) -> None:
    bot.register_callback_query_handler(
        commands_callback.send_menu,
        func=lambda c: c.data.startswith('commands')
    )

    logger.info('callback_query_handlers registered')


def register_all_handlers(bot: TeleBot) -> TeleBot:
    logger.info('Starting handlers registration...')
    registrer_admin_msg_handlers(bot)
    register_private_msg_handlers(bot)
    register_group_msg_handlers(bot)
    register_utils_handlers(bot)
    register_callback_query_handlers(bot)

    logger.info('Handlers registered')

    return bot
