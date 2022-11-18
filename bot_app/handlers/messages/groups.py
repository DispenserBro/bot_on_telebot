from telebot import types

from starters.register_bot import bot, logger

def answer_a(message: types.Message) -> None:
    logger.info('answer_a triggered in chat %s', message.chat.id)
    sticker_set = bot.get_sticker_set('bad_n_worse')  # f_093hibex_407273577_by_fStikBot

    bot.send_sticker(
        message.chat.id,
        sticker=sticker_set.stickers[5].file_id,  # [4]
        reply_to_message_id=message.id
    )
