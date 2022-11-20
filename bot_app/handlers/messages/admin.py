# WIP content
# TODO:
# 1. Create a mute command [done, testing]
# 2. Create a ban and pardon command [done, testing]
# 3. Create a pin and unpin commands [currently working on this feature]

from time import strftime, localtime, time as now
from telebot import types

from starters.register_bot import bot, logger


def check_admin(user_id: int, chat: types.Chat) -> bool:
    lst_admins = [member.user.id for member in bot.get_chat_administrators(chat.id)]
    return user_id in lst_admins


def parse_time_string(time_str: str) -> int:
    time_multiplier = {
        'm': 60,
        'h': 3600,
        'd': 86400
    }

    result = 0

    if time_str[:-1].isdigit():
        result = int(time_str[:-1]) * time_multiplier.get(time_str[-1], 0)

    return result


def mute_with_id(user_id: int, message: types.Message, time: int=60, reason: str='') -> None:
    if reason:
        reason = '\n\nПричина: ' + reason

    if user_id != message.from_user.id and not check_admin(user_id, message.chat):
            until = now() + time
            bot.restrict_chat_member(
                message.chat.id,
                user_id,
                until_date=until
            )

            time_str = strftime('%d\.%m\.%Y %H:%M', localtime(until))

            bot.delete_message(
                message.chat.id,
                message.reply_to_message.id
            )

            bot.delete_message(
                message.chat.id,
                message.id
            )

            bot.send_message(
                message.chat.id,
                f'[Пользователь](tg://user?id={user_id})\nНе может писать до\n{time_str}' + reason,
                parse_mode='MarkdownV2'
            )

    else:
        bot.delete_message(
            message.chat.id,
            message.id
        )
        
        bot.send_message(
            message.chat.id,
            f'@{message.from_user.username}\n\nНекого затыкать!'
        )


def admin_mute_member(message: types.Message) -> None:
    logger.warning(f'admin_mute_member triggered by user with id {message.from_user.id}')

    if check_admin(message.from_user.id, message.chat):
        data = message.text.split()

        if message.reply_to_message:
            user_to_mute = message.reply_to_message.from_user.id

            match data:
                case ['!ro']:
                    mute_with_id(user_to_mute, message)

                case ['!ro', data_time_or_reason]:
                    if not data_time_or_reason[:-1].isdigit():
                        mute_with_id(user_to_mute, message, reason=data_time_or_reason)
                        return

                    else:
                        parsed_time = parse_time_string(data_time_or_reason)
                        if not parsed_time:
                            bot.delete_message(
                                message.chat.id,
                                message.id
                            )

                            bot.send_message(
                                message.chat.id,
                                f'@{message.from_user.username}\n\nНеправильное время'
                            )

                            return

                        mute_with_id(user_to_mute, message, parsed_time)

                case ['!ro', time, *reason]:
                    parsed_time = parse_time_string(time)
                    if not parsed_time:
                        bot.delete_message(
                            message.chat.id,
                            message.id
                        )

                        bot.send_message(
                            message.chat.id,
                            f'@{message.from_user.username}\n\nНеправильное время'
                        )

                        return

                    mute_with_id(user_to_mute, message, parsed_time, ' '.join(reason))

                case _:
                    bot.delete_message(
                        message.chat.id,
                        message.id
                    )
                    
                    bot.send_message(
                        message.chat.id,
                        f'@{message.from_user.username}\n\nНеправильно написана команда'
                    )

        else:
            bot.delete_message(
                message.chat.id,
                message.id
            )
            
            bot.send_message(
                message.chat.id,
                f'@{message.from_user.username}\n\nНекого затыкать!'
            )

    else:
        bot.reply_to(message, 'Ты не админ этого чата!')


def admin_ban_member(message: types.Message) -> None:
    logger.warning(f'admin_ban_member triggered by user with id {message.from_user.id}')

    if check_admin(message.from_user.id, message.chat):
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id

            if user_id != message.from_user.id and not check_admin(user_id, message.chat):
                bot.ban_chat_member(message.chat.id, user_id)

                bot.delete_message(
                    message.chat.id,
                    message.reply_to_message.id
                )

                bot.delete_message(
                    message.chat.id,
                    message.id
                )

                bot.send_message(
                    message.chat.id,
                    f'[Пользователь](tg://user?id={user_id})\nЗабанен [администратором](tg://user?id={message.from_user.id})\!',
                    parse_mode='MarkdownV2'
                )

                return

        bot.reply_to(message, 'Так забанить не получится!')

        return

    bot.reply_to(message, 'Ты не админ этого чата!')


def admin_pardon_member(message: types.Message) -> None:
    logger.warning(f'admin_pardon_member triggered by user with id {message.from_user.id}')

    if check_admin(message.from_user.id, message.chat):
        if message.reply_to_message:
            print(message.reply_to_message.html_text)

        if len(message.text.split()) == 2:
            user_id = message.text.split()[1]

            if not user_id.isdigit():
                bot.reply_to(message, 'Так разбанить не получится!')

                return

            user_id = int(user_id)

            if user_id != message.from_user.id and not check_admin(user_id, message.chat):
                bot.unban_chat_member(message.chat.id, user_id, True)

                bot.delete_message(
                    message.chat.id,
                    message.id
                )

                bot.send_message(
                    message.chat.id,
                    f'[Пользователь](tg://user?id={user_id})\nРазбанен [администратором](tg://user?id={message.from_user.id})\!',
                    parse_mode='MarkdownV2'
                )

                return

        bot.reply_to(message, 'Так разбанить не получится!')

        return

    bot.reply_to(message, 'Ты не админ этого чата!')
