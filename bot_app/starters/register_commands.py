from handlers.utils.weather import send_weather_image, send_w2_info
from handlers.messages.private import send_help
from handlers.callback_handlers.commands_callback import send_menu
from starters.get_commands_dict import commands_dict as ALL_COMMANDS


def register_handlers(bot):
    bot.register_message_handler(
        send_help,
        commands=ALL_COMMANDS['help']['commands'],
        chat_types=['private']
    )

    bot.register_message_handler(
        send_weather_image,
        commands=ALL_COMMANDS['weather1']['commands']
    )

    bot.register_message_handler(
        send_w2_info,
        commands=ALL_COMMANDS['weather2']['commands']
    )

    bot.register_callback_query_handler(
        send_menu,
        func=lambda c: c.data.startswith('commands')
    )
    return bot
